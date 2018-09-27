# coding: utf-8

u"""
Jsonデータの読み込み
Wikipedea記事のJSONファイルを読み込み、「イギリス」に関する記事本文を表示せよ。
問題21-29では、ここで抽出した記事本文に対して実行せよ。
"""

import json

def extract(title):
    file = open('./jawiki-country.json', 'r')
    for line in file:
        article = json.loads(line)
        if article['title'] == title:
            return article['text']
            break
