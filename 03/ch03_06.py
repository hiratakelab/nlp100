# coding: utf-8

u"""
テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ。
"""

import ch03_01
import re

text = ch03_01.extract('イギリス')

pattern = re.compile(r'''
    ^\{\{基礎情報.*?$   # '{{基礎情報'で始まる行
    (.*?)       # キャプチャ対象、任意の0文字以上、非貪欲
    ^\}\}$      # '}}'の行
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

contents = pattern.findall(text)

pattern = re.compile(r'''
    ^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

fields = pattern.findall(contents[0])

dic = {}
for k, v in fields:
    dic[k] = v
    print(k, v)