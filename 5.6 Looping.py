# 5.6. ループのテクニック =========================

# items() メソッドを使うと、
# キーとそれに対応する値を同時に取り出せます
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# gallahad the pure
# robin the brave

# =========================
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

'''
0 tic
1 tac
2 toe
'''

# =========================
# 2またはそれ以上のシーケンス型を同時にループするために、
# zip() を使って 各要素を ひと組みに することができます

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

'''
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
'''

# =========================
for i in reversed(range(1, 10, 2)):
    print(i)

'''
9
7
5
3
1
'''

# =========================
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for i in sorted(basket):
    print(i)

'''
apple
apple
banana
orange
orange
pear
'''

# =========================
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(set(basket)):
    print(f)

'''
apple
banana
orange
pear
'''

# =========================
import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data
# [56.2, 51.7, 55.3, 52.5, 47.8]
