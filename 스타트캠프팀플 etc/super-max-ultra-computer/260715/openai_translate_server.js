// Simple Express proxy for OpenAI Translation requests
// Usage:
// 1. Install: npm init -y && npm install express node-fetch dotenv
// 2. Create .env with OPENAI_API_KEY=your_key
// 3. Run: node openai_translate_server.js

const express = require('express');
require('dotenv').config();

// Use global fetch if available (Node 18+), otherwise try to require node-fetch (v2 compatible)
let fetchFunc = null;
if (typeof fetch === 'function') {
  fetchFunc = fetch;
} else {
  try {
    fetchFunc = require('node-fetch');
  } catch (e) {
    console.error('node-fetch is not installed and global fetch is not available. Install node-fetch (v2) or use Node 18+');
    process.exit(1);
  }
}

const app = express();
app.use(express.json());

const OPENAI_KEY = process.env.OPENAI_API_KEY;
if (!OPENAI_KEY) {
  console.error('OPENAI_API_KEY not set in environment. Create a .env file with OPENAI_API_KEY=...');
  process.exit(1);
}

app.post('/translate', async (req, res) => {
  try {
    const { text, target } = req.body;
    if (!text) return res.status(400).json({ error: 'text required' });
    const endpoint = 'https://api.openai.com/v1/chat/completions';
    const body = {
      model: 'gpt-4o-mini-translator',
      messages: [
        {
          role: 'system',
          content: `You are a translator that receives prompts requiring JSON output. Translate the provided text into ${target} and respond with only a valid JSON object containing the keys "translatedTitle" and "translatedAddr". Do not include any extra text outside the JSON object.`
        },
        { role: 'user', content: text }
      ],
      max_tokens: 1200,
      temperature: 0.2
    };

    const r = await fetchFunc(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${OPENAI_KEY}`
      },
      body: JSON.stringify(body)
    });
    const data = await r.json();
    // Extract assistant reply
    const reply = data?.choices?.[0]?.message?.content || '';
    res.json({ translation: reply, raw: data });
  } catch (err) {
    fetchFunc = require('node-fetch');
    // node-fetch v3 may export as { default: fetch }, handle that
    if (fetchFunc && typeof fetchFunc !== 'function' && fetchFunc.default) fetchFunc = fetchFunc.default;
    res.status(500).json({ error: err.message });
  }
});

const PORT = process.env.PORT || 3000;
// Health endpoint for quick connectivity checks
app.get('/', (req, res) => res.send({ status: 'ok', env: process.env.NODE_ENV || 'dev' }));

// Bind to 0.0.0.0 to ensure accessibility from different network interfaces
app.listen(PORT, '0.0.0.0', () => console.log(`Translate proxy running on http://0.0.0.0:${PORT}`));
