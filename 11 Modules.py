# 11.1. 出力のフォーマット =========================
'''
reprlib モジュールは、大きなコンテナや、深くネストしたコンテナを省略して表示する
バージョンの repr() を提供
'''
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
# "{'a', 'c', 'd', 'e', 'f', 'g', ...}"

# =========================
'''
pprint モジュールは、組み込み型やユーザ定義型をわかりやすく表示し、
表示結果が複数行にわたる場合は、改行やインデントを追加して、
データ構造がより明確になるように印字します
'''
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)
'''
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
'''

# =========================
'''
textwrap モジュールは、段落で構成された文章を、
指定したスクリーン幅にぴったり収まるように調整
'''
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))
'''
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
'''

# =========================
'''
locale モジュールは、文化により異なるデータ表現形式のデータベースにアクセスします。 locale の format() 関数の grouping 属性を使えば、
数値を適切な桁区切り文字によりグループ化された形式に変換できます:
'''
import locale

locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# 'English_United States.1252'

# get a mapping of conventions
conv = locale.localeconv()          
x = 1234567.8

locale.format("%d", x, grouping=True)
# '1,234,567'

locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)
# '$1,234,567.80'

# 11.2. 文字列テンプレート =========================
from string import Template

t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
# 'Nottinghamfolk send $10 to the ditch fund.'

# =========================
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')

'''
substitute() メソッドは、プレースホルダに相当する値が
辞書やキーワード引数にない場合に KeyError を送出します
'''
t.substitute(d)
# KeyError: 'owner'

'''
欠落したデータがあるとプレースホルダをそのままにして出力する 
safe_substitute() メソッドを使う方が適切
'''
t.safe_substitute(d)
# 'Return the unladen swallow to $owner.'

# =========================
import time, os.path

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
'''
img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
'''

# 11.3. バイナリデータレコードの操作 =========================
import struct
'''
struct モジュールでは、 pack() や unpack() といった関数を提供しています。 
以下の例では、 zipfile モジュールを使わずに、ZIP ファイルのヘッダ情報を巡回する方法を示しています。
"H" と "I" というパック符号は、それぞれ2バイトと4バイトの符号無し 整数を表しています。
"<" は、そのパック符号が standard サイズであり、
バイトオーダーがリトルエンディアンであることを示しています:
'''
with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
# show the first 3 file headers
for i in range(3):                      
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    # skip to the next header
    start += extra_size + comp_size     

# 11.4. マルチスレッディング =========================
import threading, zipfile

# スレッド処理 (threading) とは、順序的な依存関係にない複数のタスクを分割するテクニック
class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

# Wait for the background task to finish
background.join()    
print('Main program waited until background was done.')

# 11.5. ログ記録  =========================

import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

'''
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
'''
# 11.5. 弱参照  =========================
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

# create a reference
a = A(10)                   

# does not create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            

# fetch the object if it is still alive
d['primary'] # 10

# remove the one reference
del a                       

# run garbage collection right away
gc.collect() # 0

# entry was automatically removed
d['primary'] # KeyError: 'primary'

# 11.7. リスト操作のためのツール =========================
'''
array (配列) モジュールでは、array() オブジェクトを提供しています。
配列はリストに似ていますが、同じ形式のデータだけが保存できます。
以下の例では、通常 1 要素あたり 16 バイトを必要とする Python 整数型のリストの 代りに、
2 バイトの符号無しの 2 進数 (タイプコード "H") の配列を使っています:
'''
from array import array

a = array('H', [4000, 10, 700, 22222])

sum(a) # 26932

a[1:3] # array('H', [10, 700])

# =========================
'''
collections モジュールでは、deque() オブジェクトを提供しています。
リスト型に似ていますが、データの追加と左端からの取り出しが速く、
その一方で中間にある値の参照は遅くなります。
こうしたオブジェクトはキューや木構造の幅優先探索の実装に向いています
'''
from collections import deque

d = deque(["task1", "task2", "task3"])
d.append("task4")

print("Handling", d.popleft())
# Handling task1

# =========================
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)

# =========================
'''
リストの代わりの実装以外にも、標準ライブラリには
ソート済みのリストを操作するための関数を備えた 
bisect のようなツールも提供しています
'''
import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))

scores
# [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

# =========================
'''
heapq モジュールは、通常のリストでヒープを実装するための関数を提供しています。
ヒープでは、最も低い値をもつエントリがつねにゼロの位置に配置されます。
ヒープは、毎回リストをソートすることなく、最小の値をもつ要素に繰り返しアクセスする
ようなアプリケーションで便利です
'''
from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

# rearrange the list into heap order
heapify(data)                      

# add a new entry
heappush(data, -5)                 

# fetch the three smallest entries
[heappop(data) for i in range(3)]  
# [-5, 0, 1]

# 11.8. 10 進浮動小数演算 =========================
from decimal import *

round(Decimal('0.70') * Decimal('1.05'), 2)
# Decimal('0.74')

round(.70 * 1.05, 2)
# 0.73

# =========================
Decimal('1.00') % Decimal('.10')
# Decimal('0.00')

1.00 % 0.10
# 0.09999999999999995

sum([Decimal('0.1')]*10) == Decimal('1.0')
# True

sum([0.1]*10) == 1.0
# False

# =========================
getcontext().prec = 36
Decimal(1) / Decimal(7)

# Decimal('0.142857142857142857142857142857142857')

