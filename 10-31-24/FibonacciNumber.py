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

def fibonacci_number_hashu_memo(n, memo={}):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number_hashu_memo(n-1, memo) + fibonacci_number_hashu_memo(n-2, memo)

for i in range(0, 18, 1):
    print(fibonacci_number_hashu_memo(i))


# The incorrect code from the book 1.5.5
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