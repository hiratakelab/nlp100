# coding: utf-8

"""
53. Tokenization
Stanford Core NLPを用い、入力テキストの解析結果をXML形式で得よ。
また、このXMLファイルを読み込み、入力テキストを1行1単語の形式で出力せよ。
"""

import ch06_01
import ch06_02
from nltk.stem.porter import PorterStemmer

st = PorterStemmer()
for lines in ch06_01.nlp_lines():
    for line in ch06_02.nlp_word(lines):
        print ('{}\t{}'.format(line, st.stem(line)))