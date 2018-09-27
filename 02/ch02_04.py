# coding: utf-8

u"""
col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し、元のファイルの1列目と2元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ。
確認にはpasteコマンドを用いよ。

paste -d "\t" col1.txt col2.txt
"""

import codecs

col1 = open("./col1.txt", "r")
col2 = open("./col2.txt", "r")
merge = codecs.open("./merge.txt", "a", "utf-8")

c1 = []
for line in col1:
    line = line.rstrip("\n")
    c1.append(line)
c2 = []
for line in col2:
    line = line.rstrip("\n")
    c2.append(line)

for i in range(len(c1)):
    str = c1[i] + "\t" + c2[i] + "\n"
    merge.write(str)

col1.close()
col2.close()
merge.close()
