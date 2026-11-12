#!/usr/bin/env python3
"""Fetch the Korean UI face (S-Core Dream 9 Black) from S-Core's official download.

    python3 tools/fetch_ko_font.py

The licence allows free redistribution but forbids modifying the file, so the
OTF is copied byte for byte from the official archive and checked against a
pinned SHA-256. It is never subset or converted; fonts.css limits it to Hangul.
"""
import hashlib
import urllib.request
import zipfile
from io import BytesIO
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = 'https://s-core.co.kr/wp-content/uploads/2020/03/S-Core_Dream_OTF.zip'
MEMBER = 'SCDream9.otf'
SHA256 = '5c246f2a17dd1eca7ecebcae1d180e8c27108533c4ad098702904bea5aee331a'


def main():
    with urllib.request.urlopen(URL, timeout=60) as response:
        archive = zipfile.ZipFile(BytesIO(response.read()))
    data = archive.read(MEMBER)
    digest = hashlib.sha256(data).hexdigest()
    if digest != SHA256:
        raise SystemExit(f'{MEMBER}: unexpected SHA-256 {digest}; check the official release before updating')
    (ROOT / 'fonts' / MEMBER).write_bytes(data)
    print(f'{MEMBER}: {len(data) / 1024:.0f} kB, unmodified official file')


if __name__ == '__main__':
    main()
