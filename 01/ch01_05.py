# -*- coding: utf-8 -*-

u"""
n-ngram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

def ngram(text, n):
    am = []
    for i in range(len(text) - n + 1):
        am.append(text[i:n+i])
    return am

text = "I am an NLPer"
print (ngram(text, 2))
print (ngram(text.split(), 2))
