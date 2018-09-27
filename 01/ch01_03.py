# -*- coding: utf-8 -*-

#coding: utf-8

u"""
円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
という文を単語に分解し、各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

chars = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
char = chars.split(' ')
num = []
for ch in char:
    num.append(len(ch))
print(num)
