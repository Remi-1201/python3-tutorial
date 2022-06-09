# 4.8.1. デフォルトの引数値 =========================

def ask_ok(prompt, retries=1, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

result = ask_ok("Type y or n / ", retries=1, reminder='Please try again!')
print(result)

'''
Type y or n / y
True

Type y or n / n
False

Type y or n / m
Please try again!
Type y or n / k
Traceback (most recent call last): errors
'''

# 他にもいくつかの方法で呼び出せます:
# 必須の引数のみ与える
ask_ok('Do you really want to quit? ')
# the same result

# 一つのオプション引数を与える
ask_ok('OK to overwrite the file?', 2)
# "Please try again!" appears 2 times

# 全ての引数を与える
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
# "Come on, only yes or no!" appears 2 times

# =========================
# デフォルト値は、関数が定義された時点で、
# 関数を 定義している 側のスコープ で評価される

i = 5

def f(arg=i): #this
    print(arg)

i = 6
f() #5

# =========================
# デフォルト値は 1 度だけしか評価されません
# 後に続く関数呼び出しで
# 関数に渡されている引数を累積します

def f(a, L=[]):
    L.append(a)
    return L

print(f(1)) # a=1
# [1]
print(f(2)) # a=2, L=[1]
# [1, 2]
print(f(3)) # a=3, L=[1, 2]
# [1, 2, 3]

# =========================
# 後続の関数呼び出しでデフォルト値を共有したくなければ、
# 代わりに以下のように関数を書くことができます:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
# [1]
print(f(1,[2,3]))
# [2, 3, 1]