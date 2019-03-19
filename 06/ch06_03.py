# coding: utf-8

"""
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
"""

import ch06_01
import ch06_02
from nltk.stem.porter import PorterStemmer

st = PorterStemmer()
for lines in ch06_01.nlp_lines():
    for line in ch06_02.nlp_word(lines):
        print ('{}\t{}'.format(line, st.stem(line)))