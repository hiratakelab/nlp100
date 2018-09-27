#coding: utf-8

u"""
暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

def cipher(texts):
    output = ""
    for text in texts:
        if text.islower():
            output += chr(219 - ord(text))
        else:
            output += text
    return output

test = "I am Mana Ihori"
print (cipher(test))
test1 = cipher(test)
print (cipher(test1))
