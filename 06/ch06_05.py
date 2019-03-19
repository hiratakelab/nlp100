# coding: utf-8

"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""

from lxml import etree

parser = etree.XMLParser(recover=True)
tree = etree.parse('./nlp.txt.xml', parser=parser)
root = tree.getroot()

for parent in root.getiterator():
    if parent.tag == 'token':
        matome = []
        for child in parent:
            if child.tag in ['word', 'lemma', 'POS']:
                matome.append(child.text)
        print('\t'.join(matome))
