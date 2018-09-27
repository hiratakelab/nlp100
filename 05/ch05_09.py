# coding: utf-8

u"""
名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
ただし，構文木上のパスは以下の仕様を満たすものとする．
・各文節は（表層形の）形態素列で表現する
・パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．
吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
"""
import ch05_02
import codecs


def returnchar(sentence, n):
    zyutugo = ''
    for char in sentence[n].morphs:
        if char.pos != '記号':
            zyutugo += char.surface
    return zyutugo, sentence[n].dst

def recurrent(sentence, n, test):
    if sentence[n].dst == -1:
        dst = returnchar(sentence, n)
        test.append(dst[0])
    else:
        dst = returnchar(sentence, n)
        test.append(dst[0])
        recurrent(sentence, dst[1], test)


for i, sentence in enumerate(ch05_02.chunks(), 1):
    # if i != 8:
    #     continue
    for n, sen in enumerate(sentence):
        flag = 0
        zyoshi = 0
        noun = ''
        for j, char in enumerate(sen.morphs):
            if char.pos != '記号':
                noun += char.surface
            if char.pos == '名詞':
                flag = 1
        if flag == 1:
            # print(noun)
            test = []
            recurrent(sentence, sen.dst, test)
            print(noun + ' -> ' + ' -> '.join(test))
    print("-------------------------")

