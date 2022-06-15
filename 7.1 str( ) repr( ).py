# # 7. 入力と出力 =========================
# # 7.1. 出力を見やすくフォーマット ========

# year = 2016
# event = 'Referendum'

# print('Results of the {year} {event}')
# # Results of the {year} {event}

# print(f'Results of the {year} {event}')
# # Results of the 2016 Referendum

# # =========================
# # str.format() =  {  } を使って変数に代入
# # フォーマットされる対象の情報を与える必要があります
# yes_votes = 42_572_654
# no_votes = 43_132_495
# percentage = yes_votes / (yes_votes + no_votes)

# print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
# #  42572654 YES votes  49.67%

# # =========================
# s = 'Hello, world.'

# # str() は repr() と同じ値を返します
# str(s)
# # 'Hello, world.'
# repr(s)
# # "'Hello, world.'"

# # repr() 関数か str() 関数でどんな値も文字列に変換
# str(1/7)
# # '0.14285714285714285'

# x = 10 * 3.25
# y = 200 * 200

# s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
# print(s)
# # The value of x is 32.5, and y is 40000...

# # The repr() of a string adds string quotes and backslashes:
# hello = 'hello, world\n'
# hellos = repr(hello)

# print(hellos)
# # 'hello, world\n'

# # The argument to repr() may be any Python object:
# repr((x, y, ('spam', 'eggs')))
# # "(32.5, 40000, ('spam', 'eggs'))"

# # =========================
# # 7.1.1. フォーマット済み文字列リテラル

# import math

# print(f'The value of pi is approximately {math.pi:.3f}.')
# # The value of pi is approximately 3.142.

# # =========================
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

# # ':' の後ろに整数をつけると、
# # そのフィールドの最小の文字幅を指定できます
# for name, phone in table.items():
#     print(f'{name:10} ==> {phone:10d}')
# '''
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678
# '''

# =========================
# '!a' は ascii() を、 '!s' は str() を、 '
# !r' は repr() を適用します
animals = 'eels'

print(f'My hovercraft is full of {animals}.')
# My hovercraft is full of eels.

print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'.