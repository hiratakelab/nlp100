#coding: utf-8

u"""
「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ。
"""

import ch04_01

nounphrases = []
for line in ch04_01.returnkeitaiso():
    # nounphrase = {}
    # flag = -1
    # for i, sen in enumerate(line):
    #     if sen["pos"] == '名詞' and len(nounphrase) == 0 and flag == -1:
    #         nounphrase[i] = sen["base"]
    #         flag = i + 1
    #     elif sen["pos"] == '助詞' and sen["base"] == 'の' and len(nounphrase) == 1 and flag == i:
    #         nounphrase[i] = sen["base"]
    #         flag = i + 1
    #     elif sen["pos"] == '名詞' and len(nounphrase) == 2 and flag == i:
    #         nounphrase[i] = sen["base"]
    #         phrase = ''
    #         for key, noun in nounphrase.items():
    #             phrase += noun
    #         if not nounphrase in nounphrases:
    #             nounphrases.append(phrase)
    #         flag = -1
    #         nounphrase = {}
    #     else:
    #         flag = -1
    #         nounphrase = {}
    if len(line) > 2:
        for i in range(1, len(line) - 1):
            if line[i]['surface'] == 'の' and line[i - 1]['pos'] == '名詞' and line[i + 1]['pos'] == '名詞':
                chara = line[i - 1]['surface'] + 'の' + line[i + 1]['surface']
                if not chara in nounphrases:
                    nounphrases.append(chara)



print(nounphrases)