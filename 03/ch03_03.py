# coding: utf-8

u"""
カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ。
"""

import ch03_01
import re

text = ch03_01.extract('イギリス').split('\n')

pattern = r'^\[\[Category:(.*?)(\|.*)*\]\]$'

for line in text:
    true = re.search(pattern, line)
    if true is not None:
        print(true.group(1))