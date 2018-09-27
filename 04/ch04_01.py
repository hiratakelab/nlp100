# coding: utf-8

u"""
形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab)を読み込むプログラムを実装せよ。
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import codecs

def returnkeitaiso():
    file = codecs.open("neko.txt.mecab", "r", "utf-8")
    one = []
    for line in file:
        line = line.rstrip("\n")
        if line == "EOS":
            yield one
            one = []
        else:
            keitaiso = {}
            line = line.split('\t')
            keitaiso["surface"] = line[0]
            values = line[1].split(',')
            keitaiso["base"] = values[6]
            keitaiso["pos"] = values[0]
            keitaiso["pos1"] = values[1]
            one.append(keitaiso)

