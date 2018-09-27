# coding: utf-8

u"""
行数のカウント
行数をカウントせよ。確認にはwcコマンドを用いよ。

wc --lines hightemp.txt
"""
file = open("./hightemp.txt", "r")
line = 0
for i, line in enumerate(file):
    line = i
print(i + 1)