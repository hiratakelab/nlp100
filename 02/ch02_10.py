#coding: utf-8

u"""
各行の1カラム目の文字列の出現頻度を求め、
出現頻度の高い順に並べる。
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．

cut -f 1 -d " " hightemp2.txt | sort | uniq --count | sort --reverse
"""

file = open("./hightemp2.txt", "r")
lines = {}
for line in file:
    line = line.split(" ")
    if line[0] in lines:
        lines[line[0]] += 1
    else:
        lines[line[0]] = 1

for k, v in sorted(lines.items(), key=lambda x: -x[1]):
    print(k, v)