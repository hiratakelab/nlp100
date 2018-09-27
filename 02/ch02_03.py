#coding: utf-8

u"""
1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ。
確認にはcutコマンドを用いよ。

cut -f 1 -d " " hightemp2.txt
cut -f 2 -d " " hightemp2.txt
"""

import codecs

file = open("./hightemp2.txt", "r")
col1 = codecs.open("./col1.txt", "a", "utf-8")
col2 = codecs.open("./col2.txt", "a", "utf-8")

for line in file:
    line = line.split(" ")
    col1.write(line[0] + "\n")
    col2.write(line[1] + "\n")
file.close()
col1.close()
col2.close()