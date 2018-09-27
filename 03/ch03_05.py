# coding: utf-8

u"""
ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ。
"""

import ch03_01
import re

text = ch03_01.extract('イギリス').split('\n')

pattern = r'(?:File|ファイル):(.+?)\|'

for line in text:
    true = re.search(pattern, line)
    if true is not None:
        print(true.group(1))