# -*- coding: utf-8 -*-

u"""
Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

def irekae(text):
    import random
    texts = text.split()
    te = []
    for i in range(len(texts)):
        if (len(texts[i])) <= 4:
            te.append(texts[i])
        else:
            x = texts[i][1:-1]
            t = random.sample(x, len(x))
            x = texts[i][0] + ''.join(t) + texts[i][-1]
            te.append(x)
    return ' '.join(te)

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print (irekae(text))
