#!/usr/bin/env python3
"""Fetch the licensed frame from its provider; do not redistribute the bare asset."""
from pathlib import Path
from urllib.request import urlopen
import shutil

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://tryhoverify.com/images/devices/iphone_18_pro/silver.webp'
DEST = ROOT / 'src/assets/mockups/iphone-18-pro-silver.webp'
TARGET = ROOT / 'out/hurdling-club-intro/source/assets/iphone-18-pro-silver.webp'

def main():
    print('License: https://tryhoverify.com/tools/device-frames/license/')
    if not DEST.exists():
        with urlopen(URL, timeout=30) as response:
            data = response.read()
        if data[:4] != b'RIFF' or data[8:12] != b'WEBP':
            raise ValueError('Provider returned an unexpected file format')
        DEST.parent.mkdir(parents=True, exist_ok=True)
        DEST.write_bytes(data)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(DEST, TARGET)
    print('Ready:', TARGET.relative_to(ROOT))

if __name__ == '__main__':
    main()
