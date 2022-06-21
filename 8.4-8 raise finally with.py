# 8.4. 例外を送出する =========================
# raise 文を使って、特定の例外を発生させることができます

raise NameError('HiThere')
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: HiThere
'''
raise ValueError
# shorthand for 'raise ValueError()'

# =========================
# 例外が発生したかどうかを判定したいだけで、
# その例外を処理するつもりがなければ、
# 単純な形式の raise 文を使って例外を再送出させることができます:

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
'''
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
'''

8.5. 例外の連鎖 =========================

# raise 文では from を使い、例外を連鎖することができます
# exc must be exception instance or None.
raise RuntimeError from exc

# これは例外を変換するときに便利です
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

'''
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
'''
# =========================
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

'''
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
'''

# 8.7. クリーンアップ動作を定義する =========================
# finally 節がある場合、 try 文が終わる前の最後の処理を、finally 節が実行します

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
'''
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <modul
'''

# =========================
def bool_return():
    try:
        return True
    finally:
        return False

bool_return()
# False

# =========================
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

# except 節または else 節の実行中に例外が発生することがあり得ます。
# その場合も、 finally 節が実行された後に例外が再送出されます。
divide(2, 1)
# result is 2.0
# executing finally clause

divide(2, 0)
# division by zero!
# executing finally clause

divide("2", "1")
# executing finally clause
# Traceback (most recent call last):

# 8.8. 定義済みクリーンアップ処理 =========================
'''
オブジェクトのなかには、その利用の成否にかかわらず、
不要になった際に実行される標準的なクリーンアップ処理が定義されているものがあります
'''


for line in open("myfile.txt"):
    print(line, end="")
# このコードの問題点は、
# コードの実行が終わった後に不定の時間ファイルを開いたままでいることです

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
# with 文は、たとえ行の処理中に問題があったとしても、
# ファイル f は常に close されます。
