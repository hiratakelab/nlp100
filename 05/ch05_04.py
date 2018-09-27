# coding: utf-8

u"""
名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が、動詞を含む文節にかかるとき、これらを田ぶつ切り形式で抽出せよ。
ただし、句読点などの記号は出力しないようにせよ。
"""

import ch05_02

for i, sentence in enumerate(ch05_02.chunks(), 1):
    for sen in sentence:
        if sen.dst == -1:
            continue
        moto = ''
        flag = 0
        for char in sen.morphs:
            if char.pos == '名詞':
                flag = 1
            if char.pos == '記号':
                continue
            moto += char.surface
        if flag == 1:
            saki = ''
            for char in sentence[sen.dst].morphs:
                if char.pos == '動詞':
                    flag = 2
                if char.pos == '記号':
                    continue
                saki += char.surface
        if flag == 2:
            print(moto + '\t' + saki)
    print("---------------------")