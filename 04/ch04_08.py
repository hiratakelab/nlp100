#coding: utf-8

u"""
頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ。
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

list_word = allwords.most_common(10)
print(list_word)
count = list(zip(*list_word))
words = count[0]
counts = count[1]

# i = 1
# left = []
# height = []
# label = []
# for k, v in sorted(allwords.items(), key=lambda x: -x[1]):
#     left.append(i)
#     label.append(k)
#     height.append(v)
#     i += 1
#     if i == 11:
#         break
#
plt.bar(range(0, 10), counts)
plt.xticks(range(0, 10), words, fontproperties=fp)
plt.show()