# coding: utf-8

u"""
動詞の格フレーム情報の抽出
45のプログラムを改変し、述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で
出力せよ。45の仕様に加えて、以下の仕様を満たすようにせよ。
・項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
・述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，
「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，
次のような出力になるはずである．
始める　で　ここで
見る　は　を　吾輩は　ものを
"""
import ch05_02
import codecs

# output = codecs.open('output.txt', 'a', 'utf-8')

for i, sentence in enumerate(ch05_02.chunks(), 1):
    for sen in sentence:
        flag = 0
        zyoshi = 0
        for char in sen.morphs:
            if char.pos == '動詞':
                moto = char.base
                flag = 1
        if flag == 1:
            saki = []
            kou = []
            for j in sen.srcs:
                mozi = ''
                for char in sentence[j].morphs:
                    if char.pos != '記号':
                        mozi += char.surface
                    if char.pos == '助詞':
                        most = char.base
                        zyoshi = 1
                        flag += 1
                if zyoshi == 1:
                    saki.append(most)
                    kou.append(mozi)
                    zyoshi = 0
        if flag > 1:
            peir = moto + '\t' + ' '.join(saki) + '\t' + ' '.join(kou)
            print(peir)
            # output.write(peir)
            # output.write('\n')
