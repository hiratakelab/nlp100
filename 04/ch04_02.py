#coding: utf-8

u"""
動詞
動詞の表層系をすべて抽出せよ。
"""

import ch04_01

verbs = []
for line in ch04_01.returnkeitaiso():
    for sen in line:
        if sen["pos"] == '動詞':
            if not sen["surface"] in verbs:
                verbs.append(sen["surface"])
print(verbs)
