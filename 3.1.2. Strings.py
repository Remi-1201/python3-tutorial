'spam eggs'  # single quotes
# 'spam eggs'

'doesn\'t'  # use \' to escape the single quote...
# "doesn't"
"doesn't"  # ...or use double quotes instead
# "doesn't"
=========================

' "Yes," they said. '
# ' "Yes," they said. '

" \"Yes,\" they said. "
# ' "Yes," they said. '

' "Isn\'t," they said. '
# ' "Isn\'t," they said. '

=========================

' "Isn\'t," they said. '
# ' "Isn\'t," they said. '
print('"Isn\'t," they said.')
# "Isn't," they said.

s = 'First line.\nSecond line.'  
# \n means newline
# without print(), \n is included in the output
s  
'First line.\nSecond line.'

# with print(), \n produces a new line
print(s)  
# First line.
# Second line.

=========================

# \ に続く文字を特殊文字として解釈されたくない場合は、
# 最初の引用符の前に r を付けた raw strings が使えます

print('C:\some\name')  
# here \n means newline!
C:\some
ame

print(r'C:\some\name') 
# note the r before the quote
C:\some\name

=========================

# 文字列リテラルは複数行にまたがって書けます。
# 1 つの方法は三連引用符 ("""...""" や '''...''') を使うことです。
# 改行文字は自動的に文字列に含まれますが、
# 行末に \ を付けることで含めないようにすることもできます

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

""" (result)
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""

=========================

# 文字列は + 演算子で連結させる (くっつけて一つにする) ことができ、
# * 演算子で反復させることができます:

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
# 'unununium'

=========================

'Py' 'thon'
# 'Python'

text = ('Put several strings within parentheses '
        'to have them joined together.')
text
# 'Put several strings within parentheses to have them joined together.'

=========================

# 連続して並んでいる複数の 文字列リテラル
#  (つまり、引用符に囲われた文字列) は、
# 変数や式には働きません

prefix = 'Py'
prefix 'thon'  
# can't concatenate a variable and a string literal
"""
  File "<stdin>", line 1
    prefix 'thon'
                ^
SyntaxError: invalid syntax
"""

('un' * 3) 'ium'
"""
  File "<stdin>", line 1
    ('un' * 3) 'ium'
                   ^
SyntaxError: invalid syntax
"""

# 変数どうしや変数とリテラルを連結したい場合は、+ を使ってください:
prefix = 'Py'
prefix + 'thon'
# 'Python'

=========================

# 文字列は インデックス (添字) を指定して文字を取得できます
word = 'Python'
word[0]  # character in position 0
'P'
word[5]  # character in position 5
'n'
word[-1]  # last character
'n'
word[-2]  # second-last character
'o'
word[-6]
'P'

# スライス は部分文字列を取得します
word = 'Python'
word[0:2]  
# characters from position 0 (included) to 2 (excluded)
'Py'
word[2:5]  
# characters from position 2 (included) to 5 (excluded)
'tho'

word[:2]   
# character from the beginning to position 2 (excluded)
'Py'
word[4:]   
# characters from position 4 (included) to the end
'on'
word[-2:]  
# characters from the second-last (included) to the end
'on'

#  s[:i] + s[i:] は常に s と等しくなります
word[:2] + word[2:]
'Python'
word[:4] + word[4:]
'Python'

# 大き過ぎるインデックスを使おうとするとエラーが発生します
# しかし、スライスで範囲外のインデックスを使ったときは、上手く対応して扱ってくれます:
word[4:42]
'on'
word[42:]
''

=========================

# Python の文字列は変更できません -- つまり 不変 です
word[0] = 'J'
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
'''
word[2:] = 'py'
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
'''

# 元の文字列と別の文字列が必要な場合は、新しく文字列を作成してください
'J' + word[1:]
'Jython'
word[:2] + 'py'
'Pypy

# 組込み関数 len() は文字列の長さ (length) を返します:
s = 'supercalifragilisticexpialidocious'
len(s) # 34


