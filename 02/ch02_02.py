# coding: utf-8

u"""
タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ。
確認にはsedコマンド、trコマンド、もしくわexpandコマンドを用いよ。

sed 's/\t/ /g' hightemp.txt
"""

import codecs

file = open("./hightemp.txt", "r")
output = codecs.open("./hightemp2.txt", "a", "utf-8")
for line in file:
    line = line.replace('\t', ' ')
    output.write(line)
    print(line, end='')
file.close()
output.close()