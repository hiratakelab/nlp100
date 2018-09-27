# coding: utf-8

"""
50. 文区切り
(. or ; or : or ? or !)→空白文字→英大文字とういうパターンを文の区切りとみなし、入力された文書を1行1文の形式で出力せよ。
"""

import codecs
import re

def nlp_lines():
    pattern = r'(^.*?[\.|;|:|\?|!])(\s)([A-Z].*)'
    with codecs.open('./nlp.txt', 'r', 'utf-8') as input:
        for line in input:
            line = line.strip()
            while len(line) > 0:
                match = re.match(pattern, line)
                if match:
                    yield match.group(1)
                    line = match.group(3)
                else:
                    yield line
                    line = ''

# for line in nlp_lines():
#     print(line)