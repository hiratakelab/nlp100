#coding: utf-8

u"""
サ変名詞
サ変接続の名詞をすべて抽出せよ。
"""

import ch04_01

nouns = []
for line in ch04_01.returnkeitaiso():
    for sen in line:
        if sen["pos"] == '名詞' and sen["pos1"] == 'サ変接続':
            if not sen["base"] in nouns:
                nouns.append(sen["base"])
print(nouns)
