# coding: utf-8

u"""
動詞の格パターンの抽出
今回用いている文章をコーパスとみなし、日本語の述語が取りうる格を調査したい。
動詞を述語、動詞にかかっている文節の助詞を格と考え、述語と格をタブ区切り形式で出力せよ。
ただし、出力は以下の仕様を満たすようにせよ。
・動詞を含む文節において、最左の動詞の基本形を述語とする
・述語に係る助詞を格とする
・述語に係る助詞（文節）が複数あるときは、すべての助詞をスペース区切りで辞書順に並べる
「吾輩はここで始めて人間というものを見た」という例文を考える。
この文は「始める」と「見る」の2つの動詞を含み、「始める」に係る文節は「ここで」、「見る」に係る文節は
「吾輩は」と「ものを」と解析された場合には、次のような出力になるはずである。
始める　で
見る　は　を
このプログラムの出力をファイルに保存し、以下の事項をUNIXコマンドを用いて確認せよ。
・コーパス中で頻出する述語と格パターンの組み合わせ
・「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）

sort output.txt | uniq -c | sort -r > sort.txt
grep '^する\s' output.txt | sort | uniq -c | sort -r > suru.txt
grep '^みる\s' output.txt | sort | uniq -c | sort -r > miru.txt
grep '^与える\s' output.txt | sort | uniq -c | sort -r > ataeru.txt
"""
import ch05_02
import codecs

output = codecs.open('output.txt', 'a', 'utf-8')

for i, sentence in enumerate(ch05_02.chunks(), 1):
    for sen in sentence:
        flag = 0
        for char in sen.morphs:
            if char.pos == '動詞':
                moto = char.base
                flag = 1
        if flag == 1:
            saki = []
            for j in sen.srcs:
                for char in sentence[j].morphs:
                    if char.pos == '助詞':
                        saki.append(char.base)
                        flag += 1
        if flag > 1:
            peir = moto + '\t' + ' '.join(saki)
            output.write(peir)
            output.write('\n')
