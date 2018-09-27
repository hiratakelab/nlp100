# coding: utf-8

u"""
名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．
・問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
・文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．
・文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
・上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．
Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
"""
import ch05_02
import codecs


def returnchar(sentence, n, ni, nj):
    zyutugo = ''
    for char in sentence[n].morphs:
        if char.pos == '記号':
            continue
        if n == ni:
            if char.pos == '名詞':
                zyutugo = 'X'
            # elif char.pos in ['助詞', '助動詞']:
            #     zyutugo += char.surface
        elif n == nj:
            if char.pos == '名詞':
                zyutugo = 'Y'
            # elif char.pos in ['助詞', '助動詞']:
            #     zyutugo += char.surface
        else:
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
    if i != 10:
        continue
    nouns = {}
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
            nouns[n] = noun

    values = list(nouns.keys())
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            flag = 0
            ni = values[i]
            nj = values[j]
            test = []
            if sentence[ni].dst >= nj:
                end = sentence[ni].dst
                fst = nj
                if end - ni > 1:
                    flag = 1
            else:
                end = nj
                fst = ni + 1

            for n in range(fst, end + 1):
                if (n < nj and n in values):
                    continue
                test.append(returnchar(sentence, n, ni, nj)[0])
            if flag == 1 and len(test) > 2:
                print(returnchar(sentence, ni, ni, nj)[0] + ' | ' + ' -> '.join(test[:-1]) + ' | ' + test[-1])
            else:
                print(returnchar(sentence, ni, ni, nj)[0] + ' -> ' + ' -> '.join(test))


