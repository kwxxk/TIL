Translate JSON helper

This folder contains a script to add language-specific fields to the JSON files in `260715/`.

Usage:

1. Ensure you have Python 3 installed.
2. (Optional) If you prefer no network calls, open `translate_jsons.py` and set `USE_NETWORK = False`.
3. Run:

```bash
python tools/translate_jsons.py
```

Behavior:
- Creates a backup `.bak` of each JSON file before overwriting.
- Adds `title_en`, `title_ja`, `title_zh`, `addr1_en`, `addr1_ja`, `addr1_zh` for each item that doesn't already have them.
- Uses https://libretranslate.de as the default translator. If that service is unreachable, it will fall back to copying the Korean text to target fields (so UI will at least show something).

If you want higher-quality translations, consider running a variant that uses OpenAI with your API key (not included in this script).