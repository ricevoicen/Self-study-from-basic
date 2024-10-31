
1.5.6   Testing 1.5.6 测试

Testing a function is the act of verifying that the function's behavior matches expectations. Our language of functions is now sufficiently complex that we need to start testing our implementations.
测试函数的行为是验证函数的行为是否符合预期。现在，我们的函数语言已经足够复杂，我们需要开始测试我们的实现。

A test is a mechanism for systematically performing this verification. Tests typically take the form of another function that contains one or more sample calls to the function being tested. The returned value is then verified against an expected result. Unlike most functions, which are meant to be general, tests involve selecting and validating calls with specific argument values. Tests also serve as documentation: they demonstrate how to call a function and what argument values are appropriate.
测试是一种系统执行此验证的机制。测试通常采用另一种函数的形式，该函数包含一个或多个对被测试函数的示例调用。随后，返回值会与预期结果进行比对。与大多数旨在通用的函数不同，测试涉及选择并验证具有特定参数值的调用。测试还充当文档：它们展示了如何调用函数以及哪些参数值是合适的。

Assertions. Programmers use assert statements to verify expectations, such as the output of a function being tested. An assert statement has an expression in a boolean context, followed by a quoted line of text (single or double quotes are both fine, but be consistent) that will be displayed if the expression evaluates to a false value.
断言。程序员使用 assert 语句来验证预期，例如测试中的函数输出。 assert 语句在布尔上下文中包含一个表达式，后面跟随一段引用的文本（单引号或双引号均可，但需保持一致），如果表达式求值为假，则显示该文本。

>>> assert fib(8) == 13, 'The 8th Fibonacci number should be 13'

When the expression being asserted evaluates to a true value, executing an assert statement has no effect. When it is a false value, assert causes an error that halts execution.
当被断言的表达式求值为真值时，执行断言语句无任何效果。若其为假值， assert 将引发错误，导致执行中断。

A test function for fib should test several arguments, including extreme values of n.
fib 的测试函数应测试多个参数，包括 n 的极值。

>>> def fib_test():
        assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
        assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
        assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'

When writing Python in files, rather than directly into the interpreter, tests are typically written in the same file or a neighboring file with the suffix _test.py.
在文件中编写 Python 代码而非直接输入解释器时，测试通常会写在同一文件或带有 _test.py 后缀的相邻文件中。

Doctests. Python provides a convenient method for placing simple tests directly in the docstring of a function. The first line of a docstring should contain a one-line description of the function, followed by a blank line. A detailed description of arguments and behavior may follow. In addition, the docstring may include a sample interactive session that calls the function:
doctests。Python 提供了一种便捷的方法，可以将简单的测试直接放在函数的文档字符串中。文档字符串的第一行应包含函数的一行描述，随后是空行。接下来可以详细描述参数和行为。此外，文档字符串还可以包含调用函数的示例交互会话：

>>> def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total

Then, the interaction can be verified via the doctest module. Below, the globals function returns a representation of the global environment, which the interpreter needs in order to evaluate expressions.
然后，可以通过 doctest 模块验证交互。下面， globals 函数返回全局环境的表示形式，解释器需要它来评估表达式。

>>> from doctest import testmod
>>> testmod()
TestResults(failed=0, attempted=2)

To verify the doctest interactions for only a single function, we use a doctest function called run_docstring_examples. This function is (unfortunately) a bit complicated to call. Its first argument is the function to test. The second should always be the result of the expression globals(), a built-in function that returns the global environment. The third argument is True to indicate that we would like "verbose" output: a catalog of all tests run.
要验证仅针对单个函数的 doctest 交互，我们使用一个名为 run_docstring_examples 的 doctest 函数。不幸的是，这个函数的调用有些复杂。其第一个参数是要测试的函数。第二个参数应始终是表达式 globals() 的结果，这是一个返回全局环境的内置函数。第三个参数是 True ，表示我们希望获得“详细”输出：所有运行测试的目录。

>>> from doctest import run_docstring_examples
>>> run_docstring_examples(sum_naturals, globals(), True)
Finding tests in NoName
Trying:
    sum_naturals(10)
Expecting:
    55
ok
Trying:
    sum_naturals(100)
Expecting:
    5050
ok

When the return value of a function does not match the expected result, the run_docstring_examples function will report this problem as a test failure.
当函数的返回值与预期结果不匹配时， run_docstring_examples 函数会将此问题报告为测试失败。

When writing Python in files, all doctests in a file can be run by starting Python with the doctest command line option:
在文件中编写 Python 代码时，可以通过使用 doctest 命令行选项启动 Python 来运行文件中的所有 doctests：

python3 -m doctest <python_source_file>

The key to effective testing is to write (and run) tests immediately after implementing new functions. It is even good practice to write some tests before you implement, in order to have some example inputs and outputs in your mind. A test that applies a single function is called a unit test. Exhaustive unit testing is a hallmark of good program design.
有效测试的关键在于，在新功能实现后立即编写（并运行）测试。甚至在实现之前编写一些测试也是良好的实践，以便在心中预设一些输入和输出的示例。针对单一功能的测试称为单元测试。全面的单元测试是优秀程序设计的标志。



### 简明解释

**测试函数** 是验证函数行为是否符合预期的一种方法。通过编写测试函数，我们可以确保代码在不同情况下都能正确运行。测试通常包括对被测试函数的示例调用，并验证返回值是否与预期结果一致。

**断言（Assertions）** 是用于验证预期结果的语句。如果断言中的表达式为假，程序会抛出错误并停止执行。

**doctests** 是一种将简单测试直接嵌入函数文档字符串中的方法。通过在文档字符串中包含示例调用和预期输出，可以使用 `doctest` 模块自动验证这些示例。

### 如何运用

1. **编写测试函数**：
   - 创建一个测试函数，例如 `fib_test()`，在其中使用 `assert` 语句来验证 `fib` 函数的输出是否符合预期。
   - 测试多个参数，包括边界值。

   ```python
   def fib_test():
       assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
       assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
       assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'
   ```

2. **使用 doctests**：
   - 在函数的文档字符串中添加示例调用和预期输出。

   ```python
   def sum_naturals(n):
       """Return the sum of the first n natural numbers.

       >>> sum_naturals(10)
       55
       >>> sum_naturals(100)
       5050
       """
       total, k = 0, 1
       while k <= n:
           total, k = total + k, k + 1
       return total
   ```

   - 使用 `doctest` 模块运行这些测试。

   ```python
   from doctest import testmod
   testmod()
   ```

   - 或者使用 `run_docstring_examples` 来单独测试某个函数。

   ```python
   from doctest import run_docstring_examples
   run_docstring_examples(sum_naturals, globals(), True)
   ```

3. **运行 doctests**：
   - 在命令行中使用 `python3 -m doctest <python_source_file>` 来运行文件中的所有 doctests。

通过这些方法，你可以系统地测试你的函数，确保它们在各种情况下都能正确运行，并且可以作为文档展示函数的用法和预期行为。