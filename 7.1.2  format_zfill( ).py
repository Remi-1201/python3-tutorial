# 7.1.2. 文字列の format() メソッド =========================

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"

print('{0} and {1}'.format('spam', 'eggs'))
# spam and eggs

print('{1} and {0}'.format('spam', 'eggs'))
# eggs and spam

# =========================
'''
str.format() メソッドにキーワード引数が渡された場合、
その値はキーワード引数の名前によって参照されます。
'''
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
# The story of Bill, Manfred, and Georg.

# '[]' を使って辞書のキーを参照する
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

#  '**' 記法を使ってキーワード引数として渡す
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# =========================
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

'''
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
'''

# =========================
'12'.zfill(5)
# '00012'

'-3.14'.zfill(7)
# '-003.14'

'3.14159265359'.zfill(5)
# '3.14159265359'

# 7.1.4. 古い文字列書式設定方法 =========================
import math

print('The value of pi is approximately %5.3f.' % math.pi)
# The value of pi is approximately 3.142.
