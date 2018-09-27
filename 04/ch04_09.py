#coding: utf-8

u"""
ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け。
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
        word = sen["surface"]
        allwords.update(word)
        # if not word in allwords:
        #     allwords[word] = 1
        # else:
        #     allwords[word] += 1

list_word = allwords.most_common()
count = list(zip(*list_word))[1]

# resort = {}
# for k, v in sorted(allwords.items(), key=lambda x: x[1]):
#     if v in resort:
#         resort[v] += 1
#     else:
#         resort[v] = 1
#
# x = list(resort.keys())
# y = list(resort.values())
plt.hist(count)
plt.show()