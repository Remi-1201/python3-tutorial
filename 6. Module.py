# 6. モジュール =========================
# Fibonacci numbers module

# write Fibonacci series up to n
def fib(n):    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# return Fibonacci series up to n
def fib2(n):   
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# import fibo
fibo.fib(1000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

fibo.fib2(100)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

fibo.__name__
# 'fibo'

fib = fibo.fib
fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# =========================

from fibo import fib, fib2
fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import *
fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

import fibo as fib
fib.fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import fib as fibonacci
fibonacci(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# =========================
# 6.1.1. モジュールをスクリプトとして実行する  

python fibo.py <arguments>

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

$ python fibo.py 50
# 0 1 1 2 3 5 8 13 21 34

# モジュールが import された場合は、そのコードは実行されません
import fibo

# =========================
# 6.2. 標準モジュール
import sys
sys.ps1
'>>> '

sys.ps2
'... '

sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>

# =========================
import sys
sys.path.append('/ufs/guido/lib/python')

# =========================
# 6.3. dir() 関数

# 組込み関数 dir() は、あるモジュールがどんな名前を定義しているか
# 調べるために使われます。 
# dir() はソートされた文字列のリストを返します
import fibo, sys

dir(fibo)
# ['__name__', 'fib', 'fib2']

dir(sys)  
# ['__breakpointhook__', '__displayhook__', '__doc__' ...

# =========================
# 引数がなければ、 dir() は現在定義している名前を列挙

a = [1, 2, 3, 4, 5]

import fibo

fib = fibo.fib

dir()
# ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

# =========================
# 組込みの関数や変数の名前 = 標準モジュール builtins で定義されています

import builtins
dir(builtins)  

# ['ArithmeticError', 'AssertionError', 'AttributeError', ...

# =========================
# 6.4. パッケージ

# サブモジュール sound.effects.echo をロード
import sound.effects.echo
# このモジュールは、完全な名前で参照しなければなりません
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# サブモジュールを import するもう一つの方法
from sound.effects import echo
# 以下のように用いることができます
echo.echofilter(input, output, delay=0.7, atten=4)

# もう一つ、必要な関数や変数を直接 import する方法があります
from sound.effects.echo import echofilter
# echofilter() を直接利用できる
echofilter(input, output, delay=0.7, atten=4)

# =========================
# 6.4.1. パッケージから * を import する

# sound/effects/__init__.py
__all__ = ["echo", "surround", "reverse"]

# =========================
# 6.4.2. パッケージ内参照

from . import echo
from .. import formats
from ..filters import equalizer