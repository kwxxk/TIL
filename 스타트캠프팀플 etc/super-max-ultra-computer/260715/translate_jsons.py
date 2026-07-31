#!/usr/bin/env python3
"""
Simple JSON translator for the 260715 dataset.
- Adds `title_en`, `title_ja`, `title_zh`, `addr1_en`, `addr1_ja`, `addr1_zh` fields for each item.
- Uses LibreTranslate public instance (https://libretranslate.de) by default.
- Skips items that already have `title_en` to avoid double work.

Usage:
    python tools/translate_jsons.py

Notes:
- This script performs network calls. If you prefer not to use the network, set USE_NETWORK=False to copy Korean text into target fields.
- Creates a backup copy of each file with `.bak` suffix before overwriting.
"""
import json
import os
import time
from urllib import request, parse

SEARCH_DIRS = [
    os.path.dirname(__file__),
    os.path.join(os.path.dirname(__file__), 'aiproject'),
    os.path.join(os.path.dirname(__file__), '..')
]
LIBRE_URL = 'https://libretranslate.de/translate'
USE_NETWORK = True
TARGET_LANGS = {
    'en': 'en',
    'ja': 'ja',
    'zh': 'zh'
}

cache = {}


def translate_text(text, target):
    if not text:
        return ''
    key = (text, target)
    if key in cache:
        return cache[key]
    if not USE_NETWORK:
        cache[key] = text
        return text
    payload = json.dumps({
        'q': text,
        'source': 'ko',
        'target': target,
        'format': 'text'
    }).encode('utf-8')
    req = request.Request(LIBRE_URL, data=payload, headers={'Content-Type': 'application/json'})
    try:
        with request.urlopen(req, timeout=10) as resp:
            resp_data = json.load(resp)
            translated = resp_data.get('translatedText') or text
            cache[key] = translated
            # be polite
            time.sleep(0.35)
            return translated
    except Exception as e:
        print(f"Warning: translation failed for target={target}, text='{text[:40]}...' -> {e}")
        cache[key] = text
        return text


def process_file(path):
    print('Processing', path)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    items = data.get('items') or []
    changed = False
    for it in items:
        # If title_en already exists, skip this item
        if it.get('title_en'):
            continue
        ko_title = it.get('title') or it.get('name') or ''
        ko_addr = it.get('addr1') or it.get('address') or ''
        # add ko fields into translations (optional)
        for lang, code in TARGET_LANGS.items():
            key_title = f'title_{lang}'
            key_addr = f'addr1_{lang}'
            if key_title not in it:
                if USE_NETWORK:
                    it[key_title] = translate_text(ko_title, code)
                else:
                    it[key_title] = ko_title
                changed = True
            if key_addr not in it:
                if USE_NETWORK:
                    it[key_addr] = translate_text(ko_addr, code)
                else:
                    it[key_addr] = ko_addr
                changed = True

    if changed:
        bak = path + '.bak'
        if not os.path.exists(bak):
            os.rename(path, bak)
            print('Backup created:', bak)
            # write new file
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print('Updated:', path)
        else:
            print('Backup already exists, skipping overwrite for safety:', path)
    else:
        print('No changes for', path)


def main():
    files = []
    for d in SEARCH_DIRS:
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if f.lower().endswith('.json') and f.startswith('부산_'):
                full = os.path.join(d, f)
                if full not in files:
                    files.append(full)
    if not files:
        print('No json files found in search dirs:', SEARCH_DIRS)
        return
    for full in files:
        try:
            process_file(full)
        except Exception as e:
            print('Error processing', full, e)


if __name__ == '__main__':
    main()
