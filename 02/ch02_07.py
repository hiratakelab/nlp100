# coding: utf-8

u"""
ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り、入力のファイルを行単位でn分割せよ。
同様の処理をsplitコマンドで実現せよ。

split -l n hightemp2.txt 出力ファイル名
"""

file = open("./hightemp2.txt", "r")

lines = []
for line in file:
    line = line.rstrip("\n")
    lines.append(line)

n = input(">>>")

sum = int(n)
for i, line in enumerate(lines):
    print(line)
    if i + 1 == sum:
        print("-----------------")
        sum = sum + int(n)