# https://docs.python.org/ja/3/tutorial/introduction.html#lists

squares = [1, 4, 9, 16, 25]
squares 
[1, 4, 9, 16, 25]

squares[0]  # indexing returns the item
1
squares[-1]
25
squares[-3:]  # slicing returns a new list
[9, 16, 25]

squares[:]
[1, 4, 9, 16, 25]

squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

=========================

# 不変 な文字列とは違って、リストは可変 型です
cubes = [1, 8, 27, 65, 125]  # something's wrong here
cubes[3] = 64  # replace the wrong value
cubes
[1, 8, 27, 64, 125]

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes
[1, 8, 27, 64, 125, 216, 343]

=========================

# スライスには、代入もできます。スライスの代入で、
# リストのサイズを変更したり、全てを削除したりもできます
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
letters
['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters
[]

letters = ['a', 'b', 'c', 'd']
len(letters) # 4

=========================

# リストを入れ子 (ほかのリストを含むリストを造る) にできます
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

x
[['a', 'b', 'c'], [1, 2, 3]]
x[0]
['a', 'b', 'c']
x[0][1]
'b'