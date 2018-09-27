# coding: utf-8

u"""
強調マークアップの除去
25の処理時に、テンプレートの値からMediaWiKiの協調マークアップ（弱い強調、強調、強い強調のすべて）を除去してテキストに変換せよ。
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

pattern = re.compile(r'\'{2,5}')

dic = {}
for k, v in fields:
    v = pattern.sub('', v)
    dic[k] = v
    print(k, v)