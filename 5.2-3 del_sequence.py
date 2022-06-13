# 5.2. del 文 =========================
a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
a
# [1, 66.25, 333, 333, 1234.5]

del a[2:4]
a
# [1, 66.25, 1234.5]

del a[:]
a
# []

del a
a
# NameError: name 'a' is not defined

# 5.3. タプルとシーケンス (sequence) =========================

t = 12345, 54321, 'hello!'
t[0]
# 12345

t
# (12345, 54321, 'hello!')

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
t[0] = 88888
# TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
# ([1, 2, 3], [3, 2, 1])

# =========================
empty = ()
singleton = 'hello',    # <-- note trailing comma

len(empty) # 0

len(singleton) # 1

singleton # ('hello',)

# =========================
# タプルのパック (tuple packing)
t = 12345, 54321, 'hello!' 

# 逆の演算も可能 
x, y, z = t
