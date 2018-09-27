# coding: utf-8

u"""
係り受け木の可視化
与えられた文の係り受け木を有効グラフとして可視化せよ。
可視化には、係り受け木をDOT言語に変換し、Graphvizを用いると良い。
また、pythonから有向グラフを直接的に可視化するには、pydotを使うと良い。
"""
import pydot
import CaboCha
from graphviz import Digraph

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

def chunks(text):
    pumpkin = CaboCha.Parser("-d /usr/lib/mecab/dic/mecab-ipadic-neologd")
    tree = pumpkin.parse(text)
    lattice = tree.toString(CaboCha.FORMAT_LATTICE)
    chunk = {}
    sentence = lattice.split('\n')
    for line in sentence:
        if line == 'EOS':
            sentence = []
            for k, v in sorted(chunk.items(), key=lambda x:x[0]):
                sentence.append(v)
            return sentence
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


text = input(">>>")

def charset(sen):
    char = ''
    for mor in sen.morphs:
        if mor.pos == '記号':
            continue
        char += mor.surface
    return char

edges = []
for i, sen in enumerate(chunks(text)):
    if sen.dst != -1:
        moto = charset(sen)
        saki = charset(chunks(text)[sen.dst])
        if moto != '' and saki != '':
            edges.append(((i, moto), (sen.dst, saki)))

graph = pydot.Dot(graph_type='digraph')
for edge in edges:
    id1 = str(edge[0][0])
    label1 = str(edge[0][1])
    id2 = str(edge[1][0])
    label2 = str(edge[1][1])

    graph.add_node(pydot.Node(id1, label=label1))
    graph.add_node(pydot.Node(id2, label=label2))

    graph.add_edge(pydot.Edge(id1, id2))

for node in graph.get_node_list():
    # node.set_fontname("times.ttf" if node.get_name().isalnum() else "msgothic.ttc")
    node.set_fontname("msgothic.ttc")


graph.write_png('result.png', prog='dot')
# print(graph.to_string())