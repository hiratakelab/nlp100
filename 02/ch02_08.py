# coding: utf-8

u"""
1列目の文字列の異なり
1列目の文字列の種類を求めよ。
確認にはsort,uniqコマンドを用いよ。

cut -f 1 -d " " hightemp2.txt | sort | uniq
"""

file = open("./hightemp2.txt", "r")

col = []
for line in file:
    line = line.split(" ")
    col.append(line[0])

lines = sorted(list(set(col)))

for line in lines:
    print(line)