#coding: utf-8

u"""
先頭からn行を出力
自然数Nをコマンドライン引数などの手段で受け取り、入力の内先頭のn行だけを表示せよ。
確認にはheadコマンドを用いよ。

head -n 5 hightemp.txt
"""

n = input(">>>")
file = open("./hightemp2.txt", "r")

for i, line in enumerate(file):
    print(line, end="")
    if i + 1 == int(n):
        break