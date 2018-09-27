#coding: utf-8

u"""
単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ。

Counter: dictのサブクラスで、イテレータを渡せば{要素, カウント}の辞書を自動的に作ってくれる
"""

import ch04_01
from collections import Counter

# allwords = {}
allwords = Counter()
for line in ch04_01.returnkeitaiso():
    for sen in line:
        word = sen["surface"]
        allwords.update(word)
        # if not word in allwords:
        #     allwords[word] = 1
        # else:
        #     allwords[word] += 1

allwords = allwords.most_common()
# for k, v in sorted(allwords.items(), key=lambda x: -x[1]):
#     print(k, v)
print(allwords)