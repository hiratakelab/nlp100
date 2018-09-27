# coding: utf-8

u"""
末尾のn行を出力
自然数Nをコマンドライン引数などの手段で受け取り、
入力の内末尾のn行だけを表示せよ。
確認にはtaileコマンドを用いよ。

tail -n 3 hightemp.txt
"""

n = input(">>>")
file = open("./hightemp2.txt", "r")

lines = []
for line in file:
    line = line.rstrip("\n")
    lines.append(line)

start = len(lines) - int(n)
for i in range(start, len(lines)):
    print(lines[i])
