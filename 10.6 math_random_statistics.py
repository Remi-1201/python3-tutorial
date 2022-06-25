# 10.6. 数学 =========================
import math

math.cos(math.pi / 4)
# 0.70710678118654757

math.log(1024, 2)
# 10.0

# =========================
'''
random モジュールは、乱数に基づいた要素選択のためのツールを提供
'''
import random
random.choice(['apple', 'pear', 'banana'])
# 'apple'

# sampling without replacement
random.sample(range(100), 10)   
# [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]

# random float
random.random()    
# 0.17970987693706186

# random integer chosen from range(6)
random.randrange(6)    
# 4

# =========================
'''
statistics モジュールは数値データの基礎的な統計的特性
（平均、中央値、分散等）を計算
'''
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

statistics.mean(data)
# 1.6071428571428572

statistics.median(data)
# 1.25

statistics.variance(data)
# 1.3720238095238095