#coding: utf-8

u"""
「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

char1 = "パトカー"
char2 = "タクシー"
char = ""
for i in range(len(char1)):
    char += char1[i] + char2[i]
print(char)
