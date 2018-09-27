# coding: utf-8

u"""
セクション構造
記事中に含まれるセクション名とそのレベル（例えば"==セクション名=="なら1)を表示せよ。
"""

import ch03_01
import re

text = ch03_01.extract('イギリス').split('\n')

pattern = r'^(={2,})\s*(.*?)\s*\1.*$'

for line in text:
    true = re.search(pattern, line)
    if true is not None:
        print(len(true.group(1)) - 1, true.group(2))