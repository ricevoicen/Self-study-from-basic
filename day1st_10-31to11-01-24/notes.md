[text](https://www.readanybook.com/online/610734#428017)

The address I am reading is as above
我正在閲讀的地址，如上

 Now we will learn about procedure definitions, a much more powerful abstraction technique by which a compound operation can be given a name and then referred to as a unit.
现在我们将学习过程定义，这是一种更为强大的抽象技术，通过它可以将复合操作赋予一个名称，然后作为一个整体来引用。

We begin by examining how to express the idea of “squaring.” We might say, “To square something, multiply it by itself.” This is expressed in our language as
我们首先探讨如何表达“平方”的概念。我们可以说：“要使某物平方，将其自身相乘。”这在我们的语言中表达为

(define (square x) (* x x))

We can understand this in the following way:
我们可以这样理解：

(define (square  x)        (*         x     x))
   ↑        ↑     ↑          ↑         ↑    ↑
 To      square something, multiply   it by itself.

We have here a compound procedure, which has been given the name square. The procedure represents the operation of multiplying something by itself. The thing to be multiplied is given a local name, x, which plays the same role that a pronoun plays in natural language. Evaluating the definition creates this compound procedure and associates it with the name square.
我们这里有一个复合过程，它被命名为 square 。该过程表示将某物自身相乘的操作。被乘的物件被赋予一个局部名称， x ，它在自然语言中扮演代词的角色。评估定义会创建这个复合过程，并将其与名称 square 关联。

This text explains how to use procedure definitions to abstract and name compound operations. Specifically, it demonstrates this concept through a simple example - the squaring operation.

### Key Point Explanations:

1. **Procedure Definition**:
   - A procedure definition is an abstraction technique that allows us to combine a series of operations and give them a name. This way, we can refer to the entire sequence of operations by this name, without having to detail each step every time.
   - For example, `square` is a procedure that represents the operation of multiplying a number by itself.

2. **Syntax for Defining a Procedure**:
   - The syntax for defining a procedure in the code is as follows:
     ```scheme
     (define (square x) (* x x))
     ```
   - This line of code means: define a procedure named `square`, which takes an argument `x`, and multiplies `x` by itself.

3. **Understanding Procedure Definitions**:
   - `(define (square x) (* x x))` can be broken down into the following parts:
     - `define`: indicates that we want to define something new.
     - `(square x)`: indicates that we want to define a procedure named `square`, which takes an argument `x`.
     - `(* x x)`: represents the body of the procedure, i.e., the part that operates on `x`. Here, `*` is the multiplication operator, and `x` is multiplied by itself.

4. **Local Name**:
   - In procedure definitions, the argument `x` is a local name, which is only valid within the procedure. This is similar to pronouns in natural language, used to refer to a certain object.
   - For example, in the `square` procedure, `x` represents the number we want to square.

5. **Creating and Associating a Procedure**:
   - When we execute the line of code `(define (square x) (* x x))`, the interpreter creates a new procedure and associates it with the name `square`. After that, we can call this procedure through the name `square`.

### Summary:
- Procedure definitions are a powerful abstraction tool that allows us to encapsulate complex operations under a single name, simplifying the writing and understanding of code.
- By defining procedures, we can break down complex operations into smaller, reusable parts, improving the readability and maintainability of code.


这段文字解释了如何使用过程定义（procedure definition）来抽象和命名复合操作。具体来说，它通过一个简单的例子——平方操作——来展示这一概念。

### 关键点解释：

1. **过程定义（Procedure Definition）**：
   - 过程定义是一种抽象技术，允许我们将一系列操作组合在一起，并赋予它们一个名称。这样，我们就可以通过这个名称来引用整个操作序列，而不需要每次都详细写出每一步。
   - 例如，`square` 是一个过程，它表示将某个数自身相乘的操作。

2. **定义过程的语法**：
   - 在代码中，定义一个过程的语法如下：
     ```scheme
     (define (square x) (* x x))
     ```
   - 这行代码的意思是：定义一个名为 `square` 的过程，它接受一个参数 `x`，并将 `x` 自身相乘。

3. **理解过程定义**：
   - `(define (square x) (* x x))` 可以分解为以下几个部分：
     - `define`：表示我们要定义一个新的东西。
     - `(square x)`：表示我们要定义一个名为 `square` 的过程，它接受一个参数 `x`。
     - `(* x x)`：表示过程的主体，即对 `x` 进行操作的部分。在这里，`*` 是乘法操作符，`x` 自身相乘。

4. **局部名称（Local Name）**：
   - 在过程定义中，参数 `x` 是一个局部名称，它只在过程内部有效。这类似于自然语言中的代词，用于指代某个对象。
   - 例如，在 `square` 过程中，`x` 代表我们要平方的那个数。

5. **创建和关联过程**：
   - 当我们执行 `(define (square x) (* x x))` 这行代码时，解释器会创建一个新的过程，并将其与名称 `square` 关联起来。之后，我们就可以通过 `square` 这个名称来调用这个过程。

### 总结：
- 过程定义是一种强大的抽象工具，允许我们将复杂的操作封装在一个名称下，从而简化代码的编写和理解。
- 通过定义过程，我们可以将复杂的操作分解为更小的、可重用的部分，提高代码的可读性和可维护性。
