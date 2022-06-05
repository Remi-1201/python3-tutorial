# 2.1.2. 対話モード
python3

# 3.1.1. 数
2 + 2
# 4
50 - 5*6
# 20
(50 - 5*6) / 4
# 5.0
8 / 5  # division always returns a floating point number
# 1.6

17 / 3  # classic division returns a float
# 5.666666666666667 
17 // 3  # floor division discards the fractional part
# 5
17 % 3  # the % operator returns the remainder of the division
# 2
5 * 3 + 2  # floored quotient * divisor + remainder
# 17

# 冪乗
5 ** 2  # 5 squared
# 25
2 ** 7  # 2 to the power of 7
# 128

# 変数に値を代入
width = 20
height = 5 * 9
width * height #900

# 複数の型が入り混じっている場合、
# 演算子は整数のオペランドを浮動小数点型に変換
4 * 3.75 - 1 
#14.0

# 最後に表示された結果は変数 _ に代入されます
tax = 12.5 / 100
price = 100.50 # this = _
price * tax
# 12.5625
price + _
# 113.0625  # this = _
round(_, 2)
# 113.06