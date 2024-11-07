#pytyon builtin functions,see: https://docs.python.org/3/library/functions.html
################################################################
#函数的定义
'''
def function_name(parameters):
    # 函数体
    # 代码逻辑
    return result  # 返回值（可选）
'''

#-------------------------------函数的参数------------------------#
"""
#位置参数（Positional Arguments）
def greet(name, message):
    print(f"Hello {name}, {message}")

greet("Alice", "Good morning")  # 输出: Hello Alice, Good morning


#默认参数（Default Arguments）
def greet(name, message="Hello"):
    print(f"Hello {name}, {message}")

greet("Alice")          # 输出: Hello Alice, Hello
greet("Bob", "Goodbye")  # 输出: Hello Bob, Goodbye


#可变参数
#*args：接受多个位置参数，将其作为元组传递。
#**kwargs：接受多个关键字参数，将其作为字典传递
def greet(*names):
    for name in names:
        print(f"Hello, {name}")

greet("Alice", "Bob", "Charlie")  # 输出: Hello, Alice Hello, Bob Hello, Charlie

def greet_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

greet_info(name="Alice", age=30)  # 输出: name: Alice age: 30

def greet(greeting, *names, **info):
    print(greeting)
    for name in names:
        print(f"Hello, {name}")
    for key, value in info.items():
        print(f"{key}: {value}")

greet("Welcome", "Alice", "Bob", name="Alice", age=30)
# 输出:
# Welcome
# Hello, Alice
# Hello, Bob
# name: Alice
# age: 30


#-------------------------------返回值------------------------#
#返回一个值
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 输出: 8

#返回多个值（元组）
def get_info():
    return "Alice", 30

name, age = get_info()
print(name)  # 输出: Alice
print(age)   # 输出: 30

#没有返回值（默认为 None）
def greet():
    print("Hello")

result = greet()
print(result)  # 输出: None

#-------------------------------作用域------------------------#
#局部作用域（Local Scope）：函数内部的变量和参数。
#全局作用域（Global Scope）：函数外部的变量。

def test():
    a = 10  # 局部变量
    print(a)

test()  # 输出: 10
################################
a = 20  # 全局变量
def test():
    print(a)

test()  # 输出: 20
###############################
a = 20
def test():
    global a
    a = 10  # 修改全局变量

test()
print(a)  # 输出: 10
###############################

#--------------------------------其他函数---------------------------#
#嵌套函数
def outer():
    a = 10
    
    def inner():
        print(f"Inner function accessing outer's variable: {a}")
    
    inner()

outer()  # 输出: Inner function accessing outer's variable: 10

##############################
#. 匿名函数（Lambda 函数） ： lambda arguments: expression

add = lambda x, y: x + y
print(add(3, 5))  # 输出: 8

##############################
#高阶函数
#例1：传递函数作为参数
def apply(func, value):
    return func(value)

result = apply(lambda x: x * 2, 5)
print(result)  # 输出: 10

#例2：返回函数
def outer():
    def inner():
        return "Hello from inner function"
    return inner

result = outer()
print(result())  # 输出: Hello from inner function
##############################
#装饰器（Decorator）
#装饰器是一个接受函数作为参数并返回一个新函数的高阶函数，常用于增强函数的功能
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def greet():
    print("Hello")

greet()  
# 输出:
# Before function call
# Hello
# After function call


#################################
#函数文档字符串（Docstring）
#每个 Python 函数可以包含一个文档字符串（docstring），用于描述该函数的功能。
#它通常位于函数体的第一行，使用三重引号 
def greet(name):
    """This function greets the person passed in as the name."""
    print(f"Hello, {name}!")

help(greet)  # 输出: help(greet) 会显示 docstring 内容


################################
#递归函数
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 输出: 120


##################################
#参数的一般顺序如下：
#可变参数 => 缺省参数 => 可变位置参数 => keyword-only 参数(可带缺省值) => 可变关键字参数
#对应下面： 1 => 3 =>(5,6) =>7 4(带缺省值) =>{'e': 8}

def func(a, b=2, *args, c, d=4, **kwargs):
    #c 是keyword-only argument, 传参必须用c=value的形式
    print(a, b, args, c, d, kwargs)

func(1, 3, 5, 6, c=7, e=8)  #output: 1 3 (5, 6) 7 4 {'e': 8}

################################################################
#参数解构
#位置参数解构（Positional Argument Unpacking）
#关键字参数解构（Keyword Argument Unpacking）

#示例 1：使用元组解构位置参数
def greet(name, age):
    print(f"Name: {name}, Age: {age}")

# 使用元组进行参数解构
data = ("Alice", 30)
greet(*data)  # 输出: Name: Alice, Age: 30

#示例 2：使用列表解构位置参数
def greet(name, age):
    print(f"Name: {name}, Age: {age}")

# 使用列表进行参数解构
data = ["Bob", 25]
greet(*data)  # 输出: Name: Bob, Age: 25

#使用字典解构关键字参数
def greet(name, age):
    print(f"Name: {name}, Age: {age}")

# 使用字典进行关键字参数解构
data = {"name": "Charlie", "age": 40}
greet(**data)  # 输出: Name: Charlie, Age: 40

#结合位置和关键字参数解构
def greet(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

data_positional = ["David", 28]  # 位置参数
data_keyword = {"city": "New York"}  # 关键字参数

greet(*data_positional, **data_keyword)  # 输出: Name: David, Age: 28, City: New York

# 解构字典中的部分键值对
def greet(name, age):
    print(f"Name: {name}, Age: {age}")

data = {"name": "Eve", "age": 22, "city": "London"}
greet(**{key: value for key, value in data.items() if key in ["name", "age"]})
# 输出: Name: Eve, Age: 22

#在函数定义中使用解构（对于传入的参数）
# 解构元组参数
def greet((name, age)):
    print(f"Name: {name}, Age: {age}")

greet(("John", 35))  # 输出: Name: John, Age: 35
"""


################################################################
#1.编写一个函数，能够接收至少两个参数，返回最小值和最大值
