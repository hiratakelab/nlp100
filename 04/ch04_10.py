#coding: utf-8

u"""
Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ。
"""

import ch04_01
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from collections import Counter

fp = FontProperties(fname=r'./ipag.ttf')

allwords = Counter()
for line in ch04_01.returnkeitaiso():
    for sen in line:
        word = sen["base"]
        allwords.update(word)
        # if not word in allwords:
        #     allwords[word] = 1
        # else:
        #     allwords[word] += 1

list_word = allwords.most_common()
counts = list(zip(*list_word))[1]

# resort = {}
# for k, v in sorted(allwords.items(), key=lambda x: x[1]):
#     if v in resort:
#         resort[v] += 1
#     else:
#         resort[v] = 1
#
# number = {}
# i = 1
# for k, v in sorted(resort.items(), key=lambda x: -x[1]):
#     number[i] = k
#     i += 1
#
# x = list(resort.keys())
# y = list(resort.values())

plt.xlim(1, len(counts) + 1)
plt.ylim(1, counts[0])

plt.scatter(range(1, len(counts) + 1), counts)
plt.xscale('log')
plt.yscale('log')
plt.show()