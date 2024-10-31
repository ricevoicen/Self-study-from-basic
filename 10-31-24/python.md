A nested expression of calls to print highlights the non-pure character of the function.
对 print 的嵌套调用表达式突显了该函数的非纯特性。

>>> print(print(1), print(2))
1
2
None None

If you find this output to be unexpected, draw an expression tree to clarify why evaluating this expression produces this peculiar output.
如果你发现这个输出出乎意料，请绘制一个表达式树来阐明为什么评估这个表达式会产生这种奇特的输出。

Be careful with print! The fact that it returns None means that it should not be the expression in an assignment statement.
小心处理 print ！它返回 None 的事实意味着它不应作为赋值语句中的表达式。

>>> two = print(2)
2
>>> print(two)
None



1.3   Defining New Functions
1.3 定义新函数
Video: Show Hide 视频：显示/隐藏

We have identified in Python some of the elements that must appear in any powerful programming language:
我们在 Python 中识别出一些必须出现在任何强大编程语言中的元素：

    Numbers and arithmetic operations are primitive built-in data values and functions.
    数字和算术运算是原始的内置数据值和函数。
    Nested function application provides a means of combining operations.
    嵌套函数应用提供了一种组合操作的方法。
    Binding names to values provides a limited means of abstraction.
    将名称绑定到值提供了有限的抽象手段。

Now we will learn about function definitions, a much more powerful abstraction technique by which a name can be bound to compound operation, which can then be referred to as a unit.
现在我们将学习函数定义，这是一种更为强大的抽象技术，通过它可以将一个名称绑定到复合操作上，然后作为一个整体来引用。



Local Names 1.3.4 本地名称
## idk_to_deepseek

One detail of a function's implementation that should not affect the function's behavior is the implementer's choice of names for the function's formal parameters. Thus, the following functions should provide the same behavior:
函数实现中的一个细节不应影响函数的行为，即实现者对函数形式参数的命名选择。因此，以下函数应提供相同的行为：

>>> def square(x):
        return mul(x, x)
>>> def square(y):
        return mul(y, y)

This principle -- that the meaning of a function should be independent of the parameter names chosen by its author -- has important consequences for programming languages. The simplest consequence is that the parameter names of a function must remain local to the body of the function.
这一原则——函数的含义应独立于其作者选择的参数名称——对编程语言具有重要影响。最直接的影响是，函数的参数名称必须保持在函数体内部。

If the parameters were not local to the bodies of their respective functions, then the parameter x in square could be confused with the parameter x in sum_squares. Critically, this is not the case: the binding for x in different local frames are unrelated. The model of computation is carefully designed to ensure this independence.
如果参数不是各自函数体内的局部变量，那么函数 square 中的参数 x 可能会与函数 sum_squares 中的参数 x 混淆。关键在于，事实并非如此：不同局部帧中 x 的绑定是互不相关的。计算模型经过精心设计，以确保这种独立性。

We say that the scope of a local name is limited to the body of the user-defined function that defines it. When a name is no longer accessible, it is out of scope. This scoping behavior isn't a new fact about our model; it is a consequence of the way environments work.
我们称局部名称的作用域限定在定义它的用户自定义函数的函数体内。当一个名称不再可访问时，它就超出了作用域。这种作用域行为并非我们模型中的新事实；它是环境工作方式的结果。


你提到的这段话确实强调了参数的局部作用域和独立性，但需要注意的是，这段话并没有说可以在同一个作用域内定义两个同名的函数。相反，它强调的是不同函数中的同名参数不会相互干扰，因为它们的作用域是独立的。

### Explanation

1. **Local Scope**:
   - The scope of parameters is limited to the body of the function that defines them. This means that parameters defined in one function do not affect parameters with the same name in other functions.
   - For example, the `x` in `square(x)` and `sum_squares(x)` are independent and do not interfere with each other.

2. **Independence**:
   - The computational model (such as the environment model) ensures that local names in different functions do not interfere with each other. Each function call creates a new local environment (or frame), which includes the local variables and parameters of that function.
   - When a function call ends, the local environment is destroyed, and the local names within it also become invalid.

### Example Explanation

#### Python Example

```python
def square(x):
    return x * x

def sum_squares(x, y):
    return square(x) + square(y)

# Call the sum_squares function
result = sum_squares(3, 4)
print(result)  # Output 25
```

- In this example, the `x` in `square(x)` and `sum_squares(x, y)` are independent.
- The `x` in `square(x)` is local to the `square` function, and the `x` and `y` in `sum_squares(x, y)` are local to the `sum_squares` function.
- When calling `sum_squares(3, 4)`, `square(x)` is called twice, calculating the squares of `3` and `4`, and then adding the results.

### Summary

- **Local Scope**: The scope of parameters is limited to the body of the function that defines them, and parameters with the same name in different functions do not interfere with each other.
- **Independence**: The computational model ensures that local names in different functions do not interfere with each other, achieved through the creation and destruction of local environments.
- **Function Overriding**: In the same scope, a second function with the same name will override the first function, so two functions with the same name cannot be defined in the same scope.

### 解释

1. **局部作用域**：
   - 参数的作用域仅限于定义它们的函数体内。这意味着在一个函数中定义的参数不会影响到其他函数中的同名参数。
   - 例如，`square(x)` 和 `sum_squares(x)` 中的 `x` 是独立的，它们不会相互干扰。

2. **独立性**：
   - 计算模型（如环境模型）确保了不同函数中的局部名称互不干扰。每个函数调用都会创建一个新的局部环境（或帧），其中包含该函数的局部变量和参数。
   - 当函数调用结束时，该局部环境会被销毁，其中的局部名称也随之失效。

### 示例解释

#### Python 示例

```python
def square(x):
    return x * x

def sum_squares(x, y):
    return square(x) + square(y)

# 调用 sum_squares 函数
result = sum_squares(3, 4)
print(result)  # 输出 25
```

- 在这个例子中，`square(x)` 和 `sum_squares(x, y)` 中的 `x` 是独立的。
- `square(x)` 中的 `x` 是局部于 `square` 函数的，`sum_squares(x, y)` 中的 `x` 和 `y` 是局部于 `sum_squares` 函数的。
- 当调用 `sum_squares(3, 4)` 时，`square(x)` 会被调用两次，分别计算 `3` 和 `4` 的平方，然后将结果相加。

### 总结

- **局部作用域**：参数的作用域仅限于定义它们的函数体内，不同函数中的同名参数不会相互干扰。
- **独立性**：计算模型确保了不同函数中的局部名称互不干扰，通过创建和销毁局部环境来实现。
- **函数覆盖**：在同一个作用域内，第二个同名函数会覆盖第一个函数，因此不能在同一个作用域内定义两个同名的函数。




1.3.5   Choosing Names 1.3.5 选择名称

The interchangeability of names does not imply that formal parameter names do not matter at all. On the contrary, well-chosen function and parameter names are essential for the human interpretability of function definitions!
名称的可互换性并不意味着形式参数名称毫无意义。相反，精心挑选的函数和参数名称对于函数定义的人类可读性至关重要！

The following guidelines are adapted from the style guide for Python code, which serves as a guide for all (non-rebellious) Python programmers. A shared set of conventions smooths communication among members of a developer community. As a side effect of following these conventions, you will find that your code becomes more internally consistent.
以下准则改编自 Python 代码风格指南，适用于所有（非叛逆的）Python 程序员。一套共享的约定有助于开发者社区成员间的沟通。遵循这些约定，你会发现你的代码内部一致性更高。

    Function names are lowercase, with words separated by underscores. Descriptive names are encouraged.
    函数名采用小写，单词之间用下划线分隔。鼓励使用描述性名称。
    Function names typically evoke operations applied to arguments by the interpreter (e.g., print, add, square) or the name of the quantity that results (e.g., max, abs, sum).
    函数名称通常唤起解释器应用于参数的操作（例如， print ， add ， square ）或结果量的名称（例如， max ， abs ， sum ）。
    Parameter names are lowercase, with words separated by underscores. Single-word names are preferred.
    参数名称为小写，单词之间用下划线分隔。优先使用单个单词的名称。
    Parameter names should evoke the role of the parameter in the function, not just the kind of argument that is allowed.
    参数名称应体现其在函数中的作用，而不仅仅是允许的参数类型。
    Single letter parameter names are acceptable when their role is obvious, but avoid "l" (lowercase ell), "O" (capital oh), or "I" (capital i) to avoid confusion with numerals.
    单字母参数名在其角色显而易见时是可以接受的，但应避免使用“l”（小写 L）、“O”（大写 O）或“I”（大写 I），以免与数字混淆。

There are many exceptions to these guidelines, even in the Python standard library. Like the vocabulary of the English language, Python has inherited words from a variety of contributors, and the result is not always consistent.
这些指南有许多例外情况，即使在 Python 标准库中也是如此。如同英语词汇一样，Python 从众多贡献者那里继承了词汇，结果并不总是保持一致。



1.3.6
Aspects of a functional abstraction. To master the use of a functional abstraction, it is often useful to consider its three core attributes. The domain of a function is the set of arguments it can take. The range of a function is the set of values it can return. The intent of a function is the relationship it computes between inputs and output (as well as any side effects it might generate). Understanding functional abstractions via their domain, range, and intent is critical to using them correctly in a complex program.
功能抽象的各个方面。要掌握功能抽象的使用，通常考虑其三个核心属性是有益的。函数的定义域是它可以接受的参数集合。函数的值域是它可以返回的值的集合。函数的意图是它计算的输入与输出之间的关系（以及它可能产生的任何副作用）。通过定义域、值域和意图来理解功能抽象，对于在复杂程序中正确使用它们至关重要。

For example, any square function that we use to implement sum_squares should have these attributes:
例如，我们用于实现 sum_squares 的任何 square 函数应具备以下特性：

    The domain is any single real number.
    该域是任意单个实数。
    The range is any non-negative real number.
    范围是任意非负实数。
    The intent is that the output is the square of the input.
    目的是输出为输入的平方。

These attributes do not specify how the intent is carried out; that detail is abstracted away.
这些属性并未规定意图如何执行；该细节已被抽象化。


## 1.4
Don't repeat yourself is a central tenet of software engineering. The so-called DRY principle states that multiple fragments of code should not describe redundant logic. Instead, that logic should be implemented once, given a name, and applied multiple times. If you find yourself copying and pasting a block of code, you have probably found an opportunity for functional abstraction.
不要重复自己是软件工程的核心原则。所谓的 DRY 原则指出，代码的多个片段不应描述冗余逻辑。相反，该逻辑应实现一次，赋予名称，并在多处应用。如果你发现自己复制粘贴了一段代码，很可能你发现了一个功能抽象的机会。


## 1.5.1
>>> def square(x):
        return mul(x, x)

Sometimes it does make sense to have a function whose body is an expression, when a non-pure function like print is called.
有时，当调用像 print 这样的非纯函数时，拥有一个函数体为表达式的函数确实是有意义的。

>>> def print_square(x):
        print(square(x))

At its highest level, the Python interpreter's job is to execute programs, composed of statements. However, much of the interesting work of computation comes from evaluating expressions. Statements govern the relationship among different expressions in a program and what happens to their results.
在最高层级，Python 解释器的工作是执行由语句组成的程序。然而，计算中有趣的工作大多来自于表达式的求值。语句管理程序中不同表达式之间的关系以及它们结果的处理方式。


#deepseek
This text and code snippets involve the concepts of function definitions, expression evaluation, statement execution, and function calls in Python. Below is a detailed explanation of these topics:

### Code Explanation

#### 1. 函数 `square`

```python
def square(x):
    return mul(x, x)
```

- **函数名称**：`square`
- **参数**：`x`
- **功能**：计算 `x` 的平方。
- **实现**：调用另一个函数 `mul(x, x)` 来计算 `x` 的平方。假设 `mul` 是一个已经定义好的函数，用于计算两个数的乘积。

#### 2. 函数 `print_square`

```python
def print_square(x):
    print(square(x))
```

- **函数名称**：`print_square`
- **参数**：`x`
- **功能**：计算 `x` 的平方并打印结果。
- **实现**：调用 `square(x)` 计算平方值，然后使用 `print` 函数将结果打印到控制台。

### 文字解释

#### 1. 函数体为表达式的函数

- **原文**：Sometimes it does make sense to have a function whose body is an expression, when a non-pure function like `print` is called.
- **解释**：有时，当调用像 `print` 这样的非纯函数时，拥有一个函数体为表达式的函数确实是有意义的。
  - **非纯函数**：非纯函数是指那些具有副作用的函数，例如修改全局状态、打印输出等。`print` 就是一个典型的非纯函数，因为它会向控制台输出内容。
  - **表达式**：表达式是计算结果的代码片段。例如，`mul(x, x)` 是一个表达式，它计算 `x` 的平方。
  - **函数体**：函数体是函数定义中的代码块。在这个例子中，`square(x)` 的函数体是一个表达式 `mul(x, x)`。

#### 2. Python 解释器的工作

- **原文**：At its highest level, the Python interpreter's job is to execute programs, composed of statements. However, much of the interesting work of computation comes from evaluating expressions. Statements govern the relationship among different expressions in a program and what happens to their results.
- **解释**：
  - **最高层级**：在最高层级，Python 解释器的工作是执行由语句组成的程序。
  - **语句**：语句是程序的基本执行单元，例如赋值语句、函数定义、条件语句等。
  - **表达式**：计算中有趣的工作大多来自于表达式的求值。表达式是计算结果的代码片段，例如算术运算、函数调用等。
  - **关系**：语句管理程序中不同表达式之间的关系以及它们结果的处理方式。例如，函数调用语句 `print(square(x))` 调用了 `square(x)` 表达式，并将结果传递给 `print` 函数。

### 总结

- **函数定义**：函数 `square` 和 `print_square` 分别用于计算平方和打印平方值。
- **表达式**：表达式是计算结果的代码片段，例如 `mul(x, x)`。
- **语句**：语句是程序的基本执行单元，管理表达式之间的关系和结果处理。
- **解释器工作**：Python 解释器执行由语句组成的程序，计算中有趣的工作大多来自于表达式的求值。

希望这个解释能帮助你理解这段代码和文字的含义。如果你有更多问题，欢迎继续提问！



### Code Explanation

#### 1. Function `square`

```python
def square(x):
    return mul(x, x)
```

- **Function Name**: `square`
- **Parameter**: `x`
- **Functionality**: Computes the square of `x`.
- **Implementation**: Calls another function `mul(x, x)` to calculate the square of `x`. It is assumed that `mul` is a predefined function used to compute the product of two numbers.

#### 2. Function `print_square`

```python
def print_square(x):
    print(square(x))
```

- **Function Name**: `print_square`
- **Parameter**: `x`
- **Functionality**: Computes the square of `x` and prints the result.
- **Implementation**: Calls `square(x)` to calculate the square value, then uses the `print` function to output the result to the console.

### Text Explanation

#### 1. Functions with Expression Bodies

- **Original Text**: Sometimes it does make sense to have a function whose body is an expression, when a non-pure function like `print` is called.
- **Explanation**: Sometimes, it makes sense to have a function whose body is an expression when calling a non-pure function like `print`.
  - **Non-pure Function**: A non-pure function is one that has side effects, such as modifying global state or producing output. `print` is a typical non-pure function because it outputs content to the console.
  - **Expression**: An expression is a code snippet that computes a result. For example, `mul(x, x)` is an expression that calculates the square of `x`.
  - **Function Body**: The function body is the block of code within the function definition. In this example, the body of `square(x)` is the expression `mul(x, x)`.

#### 2. The Role of the Python Interpreter

- **Original Text**: At its highest level, the Python interpreter's job is to execute programs, composed of statements. However, much of the interesting work of computation comes from evaluating expressions. Statements govern the relationship among different expressions in a program and what happens to their results.
- **Explanation**:
  - **Highest Level**: At the highest level, the job of the Python interpreter is to execute programs composed of statements.
  - **Statements**: Statements are the basic execution units of a program, such as assignment statements, function definitions, and conditional statements.
  - **Expressions**: Much of the interesting work in computation comes from evaluating expressions. An expression is a code snippet that computes a result, such as arithmetic operations or function calls.
  - **Relationships**: Statements manage the relationships among different expressions in a program and how their results are handled. For example, the function call statement `print(square(x))` calls the expression `square(x)` and passes the result to the `print` function.

### Summary

- **Function Definitions**: The functions `square` and `print_square` are used to compute squares and print square values, respectively.
- **Expressions**: An expression is a code snippet that computes a result, such as `mul(x, x)`.
- **Statements**: Statements are the basic execution units of a program, managing the relationships and results of expressions.
- **Interpreter's Work**: The Python interpreter executes programs composed of statements, with much of the interesting work coming from evaluating expressions.

I hope this explanation helps you understand the meaning of this code and text. If you have more questions, feel free to ask!

# Start of Selection
## The above content is arranged in the order of the book
# End of Selection

## 以上内容按照書中順序排列