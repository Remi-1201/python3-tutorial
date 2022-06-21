# =========================
# 8.1. 構文エラー(構文解析エラー (parsing error)

# while True print('Hello world')

'''
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
'''

# 上記の例では、エラーは関数 print() で検出されています。
# コロン (':') がその前に無いから

# =========================
# 8.2. 例外
# 実行中に検出されたエラーは 例外 (exception) と呼ばれる

10 * (1/0)
# ZeroDivisionError: division by zero

4 + spam*3
# NameError: name 'spam' is not defined

'2' + 2
# TypeError: can only concatenate str (not "int") to str

# =========================
# 8.3. 例外を処理する

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# まず、 try 節 (try clause) (キーワード try と except の間の文) が実行されます。
# 何も例外が発生しなければ、 except 節 をスキップして try 文の実行を終えます

except (RuntimeError, TypeError, NameError):
    pass
#  An except clause may name multiple exceptions as a parenthesized tuple

# =========================
# the following code will print B, C, D in that order

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


# =========================
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

# =========================
'''
The try ... except statement has an optional else clause, 
which, when present, must follow all except clauses. 
It is useful for code that must be executed if 
the try clause does not raise an exception
'''
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# =========================
try:
    raise Exception('spam', 'eggs')

except Exception as inst:
    print(type(inst))    
    # the exception instance
    print(inst.args)     
    # arguments stored in .args
    print(inst)          
    # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args     
    # unpack args

    print('x =', x)
    print('y =', y)

'''
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
'''
# =========================
# 例外が引数を持っていれば、それらは処理されない例外のメッセージの最後の部分
#  (「詳細説明」) に出力されます。

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# Handling run-time error: division by zero
