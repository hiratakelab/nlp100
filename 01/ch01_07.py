# -*- coding: utf-8 -*-

u"""
テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""

def moziretu(x, y, z):
    return str(x) + '時の' + str(y) + 'は' + str(z)

print (moziretu(12, '気温', 22.4))
