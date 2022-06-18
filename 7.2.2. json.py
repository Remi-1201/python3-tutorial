# 7.2.2. json による構造化されたデータの保存
# =========================

import json
# JSON (JavaScript Object Notation) = データ交換形式

# オブジェクト x があり、その JSON 形式の文字列表現を見る
x = [1, 'simple', 'list']

json.dumps(x)
# [1, "simple", "list"]

# dumps() に似た関数に、dump() があり、
# オブジェクトを text file にシリアライズします。
json.dump(x, f)
# f = 書き込み用に開かれた text file  

'''
To decode the object again,
if f is a binary file or text file object 
which has been opened for reading:
'''
x = json.load(f)
