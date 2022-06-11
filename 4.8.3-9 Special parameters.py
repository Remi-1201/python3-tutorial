# 4.8.3. 特殊なパラメータ 
# =========================

# / = only pos,  * = only kw
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      # -----------    ----------     ----------
      #   |             |                  |
      #   |        Positional or keyword   |
      #   |                                - Keyword only
      #    -- Positional only

# 4.8.3.4. 関数の例 
# =========================

def standard_arg(arg):
    print(arg)

standard_arg(2) #2

standard_arg(arg=2) #2

# =========================
def pos_only_arg(arg, /):
    print(arg)

# 引数は位置
pos_only_arg(1) #1

# 引数はキーワード
pos_only_arg(arg=1) # error
#  / が関数定義にあるので、引数は位置専用

# =========================
def kwd_only_arg(*, arg):
    print(arg)

kwd_only_arg(3) # error
# 関数定義に * があるので、引数はキーワード専用

# =========================
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

combined_example(1, 2, 3) 
# TypeError: combined_example() takes 2 positional arguments but 3 were given

combined_example(1, 2, kwd_only=3)
# 1 2 3

combined_example(1, standard=2, kwd_only=3)
# 1 2 3

combined_example(pos_only=1, standard=2, kwd_only=3)
# TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

# =========================
# 位置引数 name と name をキーとして持つ **kwds 
# の間に潜在的な衝突がある

def foo(name, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})
# TypeError: foo() got multiple values for argument 'name'

# 位置専用を示す / を使用すれば可能になります。
# name は位置引数として、そして 'name' はキーワード引数
# のキーワードとして認識されるから

# =========================
def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})
# True

# 4.8.4. 任意引数リスト
#  =========================

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
# 'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
# 'earth.mars.venus'

# 4.8.5. 引数リストのアンパック
# =========================

# normal call with separate arguments
list(range(3, 6))            
# [3, 4, 5]

# call with arguments unpacked from a list
args = [3, 6]
list(range(*args))            
# [3, 4, 5]

# =========================
# ** オペレータを使って辞書でもキーワード引数を渡すことができます
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
# -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

# 4.8.6. ラムダ式
# =========================
# キーワード lambda を使うと、名前のない小さな関数を生成できます
# 例えば lambda a, b: a+b は、二つの引数の和を返す関数です

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
# 42
f(1)
# 43

# もう1つの例では、ちょっとした関数を引数として渡すのに使っています
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# 4.8.7. ドキュメンテーション文字列
#  =========================

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
"""
Do nothing, but document it.

    No, really, it doesn't do anything.
"""

# 4.8.8. 関数のアノテーション
#  =========================

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
# Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
# Arguments: spam eggs