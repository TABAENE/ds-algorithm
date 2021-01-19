# Fibonacci with recursion, memoize and bottom up approach.

# Recursion.
def fib(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        result = fib(num - 1) + fib(num - 2)
    return result

print ("Fibonacci with recursion ...", fib(5))

# Memoize.

num = 5
memoize = {}
def fib(n, m):
    if n in m:
        return m[n]
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        result = fib(n - 1, m) + fib(n - 2, m)
    m[n] = result
    return result

print ("Fibonacci with memoize ...", fib(num, memoize))

# Bottom up approach.

def fib(num):
    memoize = {0:0, 1:1}
    for i in range(2, num + 1):
        memoize[i] = memoize[i-1] + memoize[i-2]
    return memoize[num]

print ("Fibonacci with buttom up ...", fib(num))

