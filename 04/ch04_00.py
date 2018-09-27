#coding: utf-8

u"""
neko.txtをMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ。
このファイルを用いて，以下の問いに対応するプログラムを実装せよ。
"""

import MeCab
import codecs

tagger = MeCab.Tagger('-d /usr/lib/mecab/dic/mecab-ipadic-neologd')

file = codecs.open("neko.txt", "r", "utf-8")
output = codecs.open("neko.txt.mecab", "w", "utf-8")
for line in file:
    line = line.rstrip("\n")
    result = tagger.parse(line)
    output.write(result)
file.close()
output.close()
