# coding: utf-8

u"""
機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
46のプログラムを以下の仕様を満たすように改変せよ．
・「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
・述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
・述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「別段くるにも及ばさんと、主人は手紙に返事をする。」という文から、以下の出力が得られるはずである。
返事をする　と　に　は 及ばさんと　手紙に　主人は
このプログラムの出力をファイルに保存し、以下の事項をUNIXコマンドを用いて確認せよ。
・コーパス中で頻出する述語（サ変接続名詞＋を＋動詞）
・コーパス中で頻出する述語と助詞パターン
"""
import ch05_02
import codecs

# output = codecs.open('output.txt', 'a', 'utf-8')

for i, sentence in enumerate(ch05_02.chunks(), 1):
    # if i != 949:
    #     continue
    for n, sen in enumerate(sentence):
        flag = 0
        zyoshi = 0
        for j, char in enumerate(sen.morphs):
            if len(sen.morphs) < 2:
                continue
            if sen.morphs[j - 1].pos1 == 'サ変接続' and sen.morphs[j].base == 'を':
                moto = sen.morphs[j - 1].surface + sen.morphs[j].surface
                for ch in sentence[sen.dst].morphs:
                    if ch.pos == '動詞':
                        moto += ch.base
                        anothre = sentence[sen.dst].srcs
                        skip = n
                        flag = 1
        if flag == 1:
            saki = []
            kou = []
            for j in anothre:
                if j == skip:
                    continue
                mozi = ''
                for char in sentence[j].morphs:
                    if char.pos != '記号':
                        mozi += char.surface
                    if char.pos == '助詞':
                        most = char.surface
                        zyoshi = 1
                        flag += 1
                if zyoshi == 1:
                    saki.append(most)
                    kou.append(mozi)
                    zyosi = 0
        if flag > 1:
            peir = moto + '\t' + ' '.join(saki) + '\t' + ' '.join(kou)
            print(peir)
            # output.write(peir)
            # output.write('\n')
