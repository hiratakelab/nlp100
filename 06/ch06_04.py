# cosing: utf-8

"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""

import corenlp
import pprint
import json
import dicttoxml
import codecs
from bs4 import BeautifulSoup
from lxml import etree
import ch06_01
import os


corenlp_dir = "/usr/local/lib/stanford-corenlp-full-2013-06-20/"
properties_file = "./user.properties"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir, properties= properties_file)

for line in ch06_01.nlp_lines():
    json_dict = json.loads(parser.parse(line))
    print(json_dict)
    xml = dicttoxml.dicttoxml(json_dict)
    soup = BeautifulSoup(xml, "xml")
    with codecs.open('./nlp.xml', 'w', 'utf-8') as f:
        f.write(soup.prettify())
    xparser = etree.XMLParser(recover=True)
    tree = etree.parse('./nlp.xml', parser=xparser)
    root = tree.getroot()
    data = root.findall('.//item')
    for line in data:
        if line.attrib["type"] == "str":
            line = (line.text).split('\n')
            print(line[1].strip())
    break
    # os.remove('./nlp.xml')
