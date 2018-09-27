# coding: utf-8

u"""
各行の3カラム目の数値を降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ
（この問題はコマンドで実行した時の結果と合わなくてもよい）

sort hightemp.txt --key=3,3 --numeric-sort --reverse
"""

file = open("./hightemp2.txt", "r")

lines = {}
for line in file:
    line = line.rstrip("\n")
    n = line.split(" ")
    n = float(n[2])
    if not n in lines:
        lines[n] = []
        lines[n].append(line)
    else:
        lines[n].append(line)

for k, v in sorted(lines.items(), key=lambda x: -x[0]):
    for i in v:
        print(i)
