# demo.py

def fib(n):
    """Return the nth Fibonacci number.
    
    返回第 n 个 Fibonacci 数字。
    """
    if n <= 0:
        return 0  # Return 0 if n is less than or equal to 0 # 如果 n 小于等于 0，返回 0
    elif n == 1:
        return 1  # Return 1 if n is equal to 1 # 如果 n 等于 1，返回 1
    else:
        a, b = 0, 1  # Initialize the first two Fibonacci numbers 初始化前两个 Fibonacci 数字
        for _ in range(2, n + 1):  # 从 2 到 n 进行迭代 
            a, b = b, a + b  # Update the values of a and b 更新 a 和 b 的值
        return b  # Return the nth Fibonacci number 返回第 n 个 Fibonacci 数字

def fib_test():
    """Test the fib function.
    
    测试 fib 函数。
    """
    assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'  # Assert that the 2nd Fibonacci number should be 1
# 断言第 2 个 Fibonacci 数字应为 1
    assert fib(3) == 2, 'The 3rd Fibonacci number should be 2'  # Assert that the 3rd Fibonacci number should be 2
# 断言第 3 个 Fibonacci 数字应为 2
    assert fib(50) == 12586269025, 'Error at the 50th Fibonacci number'  # Assert that the 50th Fibonacci number should be 12586269025
# 断言第 50 个 Fibonacci 数字应为 12586269025
    print("all test passed！")  # If all tests passed, print this message如果所有测试通过，打印信息

if __name__ == "__main__":
    fib_test()  # Call the fib_test function when the script is run directly
    # 当脚本直接运行时，调用 fib_test 函数
    
    
