# 4.7. 関数を定義する =========================

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

f = fib(2000)
print(f)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 

fib
f = fib
f(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 

fib(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 

# =========================

def fib2(n):  
# return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 5, 15
    while a < n:
        result.append(a)    
        # append() は result = result + [a] と等価
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
print(f100)   
# [5, 15, 20, 35, 55, 90]

