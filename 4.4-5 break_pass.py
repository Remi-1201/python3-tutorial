# 4.4. break 文と continue 文とループの else 節 =========================

# break & else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

'''
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
'''

# continue = ループの次のイテレーションを実行
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

'''
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
'''

# 4.5. pass 文 = 何もしません

while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C) 

class MyEmptyClass:
    pass 

def initlog(*args):
    pass   # Remember to implement this! 