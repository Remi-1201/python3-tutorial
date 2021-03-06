# 15. 浮動小数点演算、その問題と制限 =========================

# give 12 significant digits
format(math.pi, '.12g')  # '3.14159265359'

# give 2 digits after the point
format(math.pi, '.2f')  # '3.14'

repr(math.pi) # '3.141592653589793'

# =========================
'''
float.as_integer_ratio() メソッドは float の値を有理数として表現
有理数とは、二つの整数 a, b を用いて a/b という分数で表せる数のことをいう
'''

x = 3.14159
x.as_integer_ratio()
# (3537115888337719, 1125899906842624)

# この分数は正確なので、元の値を完全に復元することができます
x == 3537115888337719 / 1125899906842624
# True

'''
float.hex() メソッドは float の値を16進数で表現します。
この値もコンピューターが持っている正確な値を表現できます
'''
x.hex()
# '0x1.921f9f01b866ep+1'

'''
この正確な16進数表現はもとの float 値を
正確に復元するために使うことができます
'''
x == float.fromhex('0x1.921f9f01b866ep+1')
# True

# =========================
'''
合計処理における精度のロスを緩和してくれる math.fsum() 関数があります。
この関数は値を合計値に足し込みながら、 "失われた桁" を管理します。 
'''
sum([0.1] * 10) == 1.0 # False

math.fsum([0.1] * 10) == 1.0 # True

# =========================
# 15.1. 表現エラー

from decimal import Decimal
from fractions import Fraction

Fraction.from_float(0.1)
# Fraction(3602879701896397, 36028797018963968)

(0.1).as_integer_ratio()
# (3602879701896397, 36028797018963968)

Decimal.from_float(0.1)
# Decimal('0.1000000000000000055511151231257827021181583404541015625')

format(Decimal.from_float(0.1), '.17')
# '0.10000000000000001'
