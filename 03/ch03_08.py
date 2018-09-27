# coding: utf-8

u"""
内部リンクの除去
26の処理に加えて、テンプレートの値からMediaWikiの内部リンクマークアップを除去し、テキストに変換せよ。
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

pattern1 = re.compile(r'(\'{2,5})(.*?)(\1)')
pattern2 = re.compile(r'\[{2}([^|\]]+?\|)*(.*?)\]{2}')
dic = {}
for k, v in fields:
    v = pattern1.sub(r'\2', v)
    v = pattern2.sub(r'\2', v)
    dic[k] = v
    print(k, v)