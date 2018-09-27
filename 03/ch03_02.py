# coding: utf-8

u"""
カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ。
"""

import ch03_01

text = ch03_01.extract('イギリス').split('\n')

for line in text:
    if "Category" in line:
        print(line)
