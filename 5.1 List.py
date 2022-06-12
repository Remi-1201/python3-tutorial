# 5. Data Structures =========================

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple') # 2

fruits.count('tangerine') # 0

fruits.index('banana') #3

# Find next banana starting a position 4
fruits.index('banana', 4)  #6

fruits.reverse()
fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append('grape')
fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()
fruits
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

fruits.pop()
# 'pear'

# 5.1.1. リストをスタックとして使う =========================
stack = [3, 4, 5]

stack.append(6)
stack.append(7)
stack # [3, 4, 5, 6, 7]

stack.pop() # 7

stack # [3, 4, 5, 6]

stack.pop() # 6

stack.pop() # 5

stack # [3, 4]

# 5.1.2. リストをキューとして使う =========================

from collections import deque
queue = deque(["Eric", "John", "Michael"])

# 最初に追加した要素を最初に取り出します
queue.append("Terry")           
# Terry arrives

queue.append("Graham")          
# Graham arrives

queue.popleft()                 
# The first to arrive now leaves

queue.popleft()                
# The second to arrive now leaves

queue                           
# Remaining queue in order of arrival

# 5.1.3. リストの内包表記 =========================

squares = []
for x in range(10):
    squares.append(x**2)

squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = list(map(lambda x: x**2, range(10)))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# =========================

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# =========================

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
vec2 = [x*2 for x in vec]
# [-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
# [0, 2, 4]

# apply a function to all the elements
[abs(x) for x in vec]
# [4, 2, 0, 2, 4]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
# ['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]
  # File "<stdin>", line 1, in <module>
  #   [x, x**2 for x in range(6)]

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

from math import pi
[str(round(pi, i)) for i in range(1, 6)]
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']

# 5.1.4. ネストしたリストの内包表記 =========================

# 長さ4のリスト3つからなる、3x4 の matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# =========================
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# =========================
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# =========================
list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]




