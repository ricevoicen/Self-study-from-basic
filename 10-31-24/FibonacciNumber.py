#Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    one, two = 0, 1
    k = 2
    while k < n:
        one, two = two, one + two
        k += 1
    return two


for i in range(0, 18, 1):
    print(fibonacci(i))

def fibonacci_number_hashu(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number_hashu(n-1) + fibonacci_number_hashu(n-2)

#The `memo` in the code serves as a cache to store previously computed Fibonacci numbers, which helps to optimize the recursive function by avoiding redundant calculations. This technique is known as memoization.
def fibonacci_number_hashu_memo(n, memo={}):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number_hashu_memo(n-1, memo) + fibonacci_number_hashu_memo(n-2, memo)
#在代码中，`memo`的作用是作为缓存，用于存储先前计算的斐波那契数，从而通过避免重复计算来优化递归函数。这种技术被称为备忘录化（memoization）。


for i in range(0, 18, 1):
    print(fibonacci_number_hashu(i))


# The incorrect code from the book 1.5.5
# This is the first line of the code
def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    pred, curr = 0, 1   # Fibonacci numbers 1 and 2
    k = 2               # Which Fib number is curr?
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr

result = fib(8)
#书中的错误代码 1.5.5
#就是本代码第一行的那个
