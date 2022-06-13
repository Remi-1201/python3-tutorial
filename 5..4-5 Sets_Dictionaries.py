# 5.4. 集合型 =========================

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# show that duplicates have been removed
print(basket)                      
# {'orange', 'banana', 'pear', 'apple'}

# fast membership testing
'orange' in basket                 
# True

'crabgrass' in basket
# False

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

# unique letters in a
a                                  
# {'a', 'r', 'b', 'c', 'd'}

# letters in a but not in b
a - b                              
# {'r', 'd', 'b'}

# letters in a or b or both
a | b                              
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

# letters in both a and b
a & b                              
# {'a', 'c'}

# letters in a or b but not both
a ^ b                              
# {'r', 'd', 'b', 'm', 'z', 'l'}

# =========================

a = {x for x in 'abracadabra' if x not in 'abc'}

a
# {'r', 'd'}

# 5.5. 辞書型 Dictionaries =========================

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

tel
# {'jack': 4098, 'sape': 4139, 'guido': 4127}

tel['jack']
# 4098

del tel['sape']
tel['irv'] = 4127
tel
# {'jack': 4098, 'guido': 4127, 'irv': 4127}

list(tel)
# ['jack', 'guido', 'irv']

sorted(tel)
# ['guido', 'irv', 'jack']

'guido' in tel
# True

'jack' not in tel
# False

# =========================
# dict() コンストラクタは、
# キーと値のペアのタプルを含むリストから辞書を生成

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

{x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}

dict(sape=4139, guido=4127, jack=4098)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
