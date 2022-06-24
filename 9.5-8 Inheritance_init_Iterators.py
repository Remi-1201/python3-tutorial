# 9.5. 継承 =========================
# 継承の概念をサポートしない言語機能は "クラス" と呼ぶに値しません
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

class DerivedClassName(modname.BaseClassName):

# 9.5.1. 多重継承  =========================
'''
Python では、多重継承 (multiple inheritance) の形式もサポートしています。
複数の基底クラスをもつクラス定義は次のようになります。
'''
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

# 9.6. プライベート変数  =========================
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

  # private copy of original update() method
    __update = update   

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# 9.7. 残りのはしばし  =========================
class Employee:
    pass

# Create an empty employee record
john = Employee()  

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

9.8. イテレータ (iterator) =========================

for element in [1, 2, 3]:
    print(element)
'''
1
2
3
'''
for key in {'one':1, 'two':2}:
    print(key)
'''
one
two
'''
for char in "123":
    print(char)
'''
1
2
3
'''
for line in open("myfile.txt"):
    print(line, end='')

# =========================
s = 'abc'
it = iter(s)
it # <str_iterator object at 0x10c90e650>

next(it) # 'a'

next(it) # 'b'

next(it) # 'c'

next(it) # errors

# =========================
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev) # <__main__.Reverse object at 0x00A1DB50>

for char in rev:
    print(char)
'''
m
a
p
s
'''