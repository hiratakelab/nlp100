# coding: utf-8

u"""
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
"""

import codecs
import CaboCha

path = "/mnt/c/NPL100knock/04/neko.txt"
file = codecs.open(path, 'r', 'utf-8')
output = codecs.open('./neko.txt.cabocha', 'a', 'utf-8')

for line in file:
    line = line.rstrip('\n')
    pumpkin = CaboCha.Parser()
    tree = pumpkin.parse(line)
    lattice = tree.toString(CaboCha.FORMAT_LATTICE)
    output.write(lattice)
file.close()
output.close()
