# coding:utf-8

u"""
国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

import ch03_01
import re
import urllib.parse, urllib.request
import json

text = ch03_01.extract('イギリス')

pattern = re.compile(r'''
    ^\{\{基礎情報.*?$   # '{{基礎情報'で始まる行
    (.*?)       # キャプチャ対象、任意の0文字以上、非貪欲
    ^\}\}$      # '}}'の行
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

contents = pattern.findall(text)

pattern = re.compile(r'''
    ^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

fields = pattern.findall(contents[0])

# '''の削除
pattern1 = re.compile(r'(\'{2,5})(.*?)(\1)')
# [[]]の削除
pattern2 = re.compile(r'\[{2}([^|\]]+?\|)*(.*?)\]{2}')
# Template:Langの削除
pattern3 = re.compile(r'\{{2}lang(?:[^|]*?\|)*?([^|]*?)\}{2}')
# 外部リンクの削除
pattern4 = re.compile(r'\[http:\/\/(?:[^\s]*?/s)?([^]]*?)\]')
# <br>,<ref>の削除
pattern5 = re.compile(r'<\/?[br|ref][^>]*?>')
dic = {}
for k, v in fields:
    v = pattern1.sub(r'\2', v)
    v = pattern2.sub(r'\2', v)
    v = pattern3.sub(r'\1', v)
    v = pattern4.sub(r'\1', v)
    v = pattern5.sub('', v)
    dic[k] = v

flag = dic['国旗画像']

url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(flag) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

request = urllib.request.Request(url,
    headers={'User-Agent': 'NLP100_Python(@segavvy)'})
connection = urllib.request.urlopen(request)

data = json.loads(connection.read().decode())

url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url)