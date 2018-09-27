# coding: utf-8

"""
51. 単語の切り出し
空白を単語の区切りとみなし、50の出力を入力として受け取り、1行1単語の形式で出力せよ。
ただし、文の終端では空白を出力せよ．
"""

import ch06_01

def nlp_word(lines):
    lines = lines.split(' ')
    lines.append(' ')
    for line in lines:
        line = line.rstrip('.,;:?!')
        yield line

# for lines in ch06_01.nlp_lines():
#     for line in nlp_word(lines):
#         print (line)