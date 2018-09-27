#coding: utf-8

u"""
名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ。
"""

import ch04_01

nouns = []
for line in ch04_01.returnkeitaiso():
    # noun = ''
    # flag = []
    # compair = {}
    # cnt = 1
    # correct = ''
    # for i, sen in enumerate(line):
    #     # print(i)
    #     if sen["pos"] == '名詞':
    #         flag.append(i)
    #         if len(flag) == 1:
    #             noun += sen["surface"]
    #         elif i - 1 in flag:
    #             noun += sen["surface"]
    #             cnt += 1
    #             # print(i, flag)
    #         else:
    #             if cnt == 1:
    #                 continue
    #             if cnt in compair:
    #                 compair[cnt].append(noun)
    #             else:
    #                 compair[cnt] = []
    #                 compair[cnt].append(noun)
    #             noun = ''
    #             flag = []
    #             cnt = 1
    # for k, v in sorted(compair.items(), key=lambda x: -x[0]):
    #     if len(v) > 1:
    #         correct = max(v, key=len)
    #     else:
    #         correct = v[0]
    #     break
    #
    # if (not correct in nouns) and (correct != ''):
    #     nouns.append(correct)
    noun = []
    for sen in line:
        if sen['pos'] == '名詞':
            noun.append(sen['surface'])
        else:
            if len(noun) > 1:
                nouns.append(''.join(noun))
            noun = []
        if len(noun) > 1:
            nouns.append(''.join(noun))

print(set(nouns))