# coding: utf-8

u"""
集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

def ngram(text, n):
    am = []
    for i in range(len(text) - n + 1):
        am.append(text[i:n+i])
    return am

def sehantei(x):
    if "se" in x:
        print("True")
    else:
        print("False")

char1 = "paraparaparadise"
char2 = "paragraph"

x = set(ngram(char1, 2))
y = set(ngram(char2, 2))

print(x, y)
print(x | y)
print(x & y)
print(x - y)

sehantei(x)
sehantei(y)
