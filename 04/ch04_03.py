#coding: utf-8

u"""
動詞の原形
動詞の原形をすべて抽出せよ。
"""

import ch04_01

verbs = []
for line in ch04_01.returnkeitaiso():
    for sen in line:
        if sen["pos"] == '動詞':
            if not sen["base"] in verbs:
                verbs.append(sen["base"])
print(verbs)
