# 9.2.1. スコープと名前空間の例 =========================
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"

    do_local()
    print("After local assignment:", spam)
    # After local assignment: test spam       

    do_nonlocal()
    print("After nonlocal assignment:", spam)
    # After nonlocal assignment: nonlocal spam

    do_global()
    print("After global assignment:", spam)
    #After global assignment: nonlocal spam  

scope_test()
print("In global scope:", spam)
# In global scope: global spam

# 9.3.2. クラスオブジェクト =========================

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r) # 3.0
print(x.i) # -4.5

# 9.3.5. クラスとインスタンス変数 =========================
class Dog:

    kind = 'canine'         
    # class variable shared by all instances

    def __init__(self, name):
        self.name = name    
        # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

# shared by all dogs
d.kind                  
# 'canine'

# shared by all dogs
e.kind                  
# 'canine'

# unique to d
d.name                  
# 'Fido'

# unique to e
e.name                  
# 'Buddy'

# =========================
class Dog:
    # mistaken use of a class variable
    tricks = []             

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

# unexpectedly shared by all dogs
d.tricks                
# ['roll over', 'play dead']

# =========================
# このクラスの正しい設計ではインスタンス変数を代わりに使用するべきです
class Dog:

    def __init__(self, name):
        self.name = name
        # creates a new empty list for each dog
        self.tricks = []    

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
# ['roll over']
e.tricks
# ['play dead']

# 9.4. いろいろな注意点 =========================
'''
インスタンスとクラスの両方で同じ属性名が使用されている場合、
属性検索はインスタンスが優先されます。
'''
class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
# storage west

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
# storage east

# =========================
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

'''
f 、 g 、および h は、すべて C の属性であり
関数オブジェクトを参照しています。
従って、これら全ては、 C のインスタンスのメソッドとなります 
--- h は g と全く等価です
'''

# =========================
'''
メソッドは、 self 引数のメソッド属性を使って、
他のメソッドを呼び出すことができます
'''
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)