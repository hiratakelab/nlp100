# coding: utf-8

u"""
係り元と係先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""

import ch05_02

for i, sentence in enumerate(ch05_02.chunks(), 1):
    for sen in sentence:
        if sen.dst == -1:
            continue
        moto = ''
        for char in sen.morphs:
            if char.pos == '記号':
                continue
            moto += char.surface
        saki = ''
        for char in sentence[sen.dst].morphs:
            if char.pos == '記号':
                continue
            saki += char.surface
        print(moto + '\t' + saki)
    print("---------------------")