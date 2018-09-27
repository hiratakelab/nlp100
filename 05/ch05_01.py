# coding: utf-8

u"""
係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

import codecs

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

file = codecs.open('./neko.txt.cabocha', 'r', 'utf-8')
sentences = []
sentence = []
for line in file:
    line = line.rstrip('/n')
    if line.startswith('*'):
        continue
    if line == 'EOS\n':
        # if len(sentence) == 0:
        #     continue
        sentences.append(sentence)
        sentence = []
    else:
        line = line.split('\t')
        keitaiso = line[1].split(',')
        morph = Morph(line[0], keitaiso[6], keitaiso[0], keitaiso[1])
        sentence.append(morph)

for word in sentences[2]:
    print(word.surface, word.base, word.pos, word.pos1)

