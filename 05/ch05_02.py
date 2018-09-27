# coding: utf-8

u"""
係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import codecs

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []

def chunks():
    file = codecs.open('./neko.txt.cabocha', 'r', 'utf-8')
    chunk = {}
    for line in file:
        line = line.rstrip('/n')
        if line == 'EOS\n':
            sentence = []
            for k, v in sorted(chunk.items(), key=lambda x:x[0]):
                sentence.append(v)
            yield sentence
            chunk = {}
        elif line.startswith('*'):
            line = line.split(' ')
            idx = int(line[1])
            dst = int(line[2][:-1])
            if dst != -1:
                if not dst in chunk:
                    chunk[dst] = Chunk()
                chunk[dst].srcs.append(idx)
            if not idx in chunk:
                chunk[idx] = Chunk()
            chunk[idx].dst = dst
        else:
            line = line.split('\t')
            keitaiso = line[1].split(',')
            morph = Morph(line[0], keitaiso[6], keitaiso[0], keitaiso[1])
            chunk[idx].morphs.append(morph)

# for i, sentence in enumerate(chunks(), 1):
#     if i != 8:
#         continue
#     for sen in sentence:
#         sentence = ''
#         for char in sen.morphs:
#             sentence += char.surface
#         print(sentence, sen.dst, sen.srcs)

