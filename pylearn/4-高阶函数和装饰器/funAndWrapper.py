#生成器(Generator)是一种用于创建迭代器的特殊函数
# 与普通函数不同,生成器不会一次性返回所有数据,
# 而是每次迭代时动态地生成数据,从而节省内存并提高效率
# 生成器函数使用 yield 语句而不是 return 来生成一个值,
# 并在生成值后暂停执行,直到下一次调用生成器的 __next__() 方法时才恢复执行
"""
def inc():
    for i in range(3):
        yield i
    
print(type(inc))  # 输出: <class 'function'>
print(type(inc()))  # 输出: <class 'generator'>

a = inc()
print(next(a))  # 0
print(next(a)) # 1
print(next(a))  # 2
print(next(a)) # StopIteration


#yield 的作用
#与 return 不同,yield 的作用是返回一个值,并在当前位置“暂停”函数,保留函数的执行状态和局部变量
def countdown(num):
    print("Starting countdown...")
    while num > 0:
        yield num
        num -= 1

# 使用生成器
for count in countdown(5):
    print(count)

#生成器表达式
gen_expr = (x * x for x in range(5))
for num in gen_expr:
    print(num)


#优势:节省内存
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 无限序列,可以使用 break 停止
for num in fibonacci():
    if num > 100:
        break
    print(num)


##生成器方法:send()、throw() 和 close()
#send(value):可以向生成器发送一个值,用于修改生成器的内部状态
#throw(type, value=None, traceback=None):可以在生成器中引发指定类型的异常
#close():关闭生成器,触发 GeneratorExit 异常,停止生成器

def custom_generator():
    value = yield "Start"
    while True:
        value = yield f"Received {value}"

gen = custom_generator()
print(next(gen))         # 输出 "Start"
print(gen.send("Hello")) # 输出 "Received Hello"
print(gen.send("World")) # 输出 "Received World"
gen.close()              # 关闭生成器


#生成器应用 : 协程coroutine
#生成器支持 send() 方法,可以用于在生成器函数中接收外部数据,
#实现简单的协程,适用于需要中断、恢复并处理外部输入的任务
#Python中的协程主要通过 async 和 await 关键字来实现

#协程调度:两个生成器A,B next(A) 和 next(B) 交替执行
def accumulator():
    total = 0
    while True:
        x = yield total
        if x is None:
            break
        total += x

gen = accumulator()
print(next(gen))      # 初始化生成器
print(gen.send(10))   # 输出 10
print(gen.send(20))   # 输出 30
gen.close()           # 结束生成器

##yield from 是 Python 中用于简化生成器嵌套调用的语法
def sub_generator():
    yield 1
    yield 2
    return "sub_generator done"

def main_generator():
    result = yield from sub_generator()  # 捕获返回值
    print(f"sub_generator returned: {result}")
    yield 3

for value in main_generator():
    print(value)

#yield from 可以简化生成器嵌套调用的过程,具体而言,它具备以下几个重要作用:

#生成子生成器的值:可以将子生成器中的所有值逐个生成出来,而无需显式使用 for 循环
#双向通信:当生成器与调用方有数据交互时(例如通过 send() 发送数据或通过 throw() 触发异常),yield from 可以自动将数据从调用方传递到子生成器
#异常传递:如果父生成器捕获到异常,yield from 可以将异常传递给子生成器
#返回值:在 Python 3.3 之后,生成器可以使用 return 语句返回一个值,而 yield from 会捕获该返回值

"""
################################################################
"""
#高阶函数指的是能够接收其他函数作为参数或返回函数作为结果的函数,数学:y = g(f(x))

def counter(base):
    def inc(step=1):
        nonlocal base  # 声明 base 为 nonlocal
        base += step
        return base
    return inc

print(counter(10)())  # 11

"""
#################sorted自实现开始#######################
"""
#普通函数嵌套实现
lst = [1,5,3,2,4,6,7,11,9,10]
def sort(iterable,reverse=False):
    ret = []
    def comp():
        flag = item < val if not reverse else item > val
        return flag
    
    for item in iterable:
        for idx,val in enumerate(ret):
            #flag = item < val if not reverse else item > val
            if comp():
                ret.insert(idx, item)
                break
        else:
            ret.append(item)
    return ret

print(sort(lst))  # 
print(sort(lst, reverse=True))  # 

#######改造成高阶函数1#######

lst = [1,5,3,2,4,6,7,11,9,10]
def comp(a,b,reverse):
    flag = a < b if not reverse else a > b
    return flag
def sort(iterable,key=comp,reverse=False):
    ret = []
    
    
    for item in iterable:
        for idx,val in enumerate(ret):
            #flag = item < val if not reverse else item > val
            if comp(item, val, reverse):
                ret.insert(idx, item)
                break
        else:
            ret.append(item)
    return ret

print(sort(lst))  # 
print(sort(lst, reverse=True))  

#######改造成高阶函数2#######
lst = [1,5,3,2,4,6,7,11,9,10]
def sort(iterable,key=lambda a,b:a<b,reverse=False):
    ret = []
    
    for item in iterable:
        for idx,val in enumerate(ret):
            #flag = item < val if not reverse else item > val
            flag = key(item, val) if not reverse else key(val, item)
            if flag:
                ret.insert(idx, item)
                break
        else:
            ret.append(item)
    return ret
print(sort(lst))  # 
print(sort(lst, reverse=True))  
"""
#################sorted自实现结束#######################

###############################################################
"""
#zip() + map()/filter()
#zip()函数可以将多个可迭代对象组合成元组的可迭代对象,经常与map()或filter()结合使用

#filter(function, iterable):返回一个迭代器,从 iterable 中取出元素,并将元素作为参数传递给 function
f = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 1])
for num in f:
    print(f"filter object: {num}")

#map(function,*iterables):返回一个迭代器,将 function 依次作用于 iterable 的元素上
print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))

a = map(lambda x: x * 2, [1, 2, 3, 4, 5])
for num in a:
    print(f"map object: {num}")

#zip(*iterables):返回一个迭代器,将 iterables 中各个元素配对
b = zip([1, 2, 3], ['a', 'b', 'c', 'd', 'e'])
for num in b:
    print(f"zip object: {num}")
"""
################################################################
"""
#柯里化(Currying)是一种函数式编程的技术,
#它将原来接收多个参数的函数转换成一系列只接收单个参数的函数
#换句话说,柯里化后的函数每次只接收一个参数,并返回一个新函数,
#用于接收下一个参数,直到所有参数都接收完为止,最终返回计算结果
#数学形式:z=f(x,y) 转化成 z=f(x)(y)的形式

#示例:
def add(x, y):
    return x + y

def add_curry(x):
    return lambda y: x + y

def add_curr(x):
    def _add(y):
        return x + y
    return _add

add_10 = add_curry(10)
b = add_10(20)
print(b)
print(add_curry(10)(20))  # 等同于 add_10(20)
"""
################################################################
#装饰器(decorator)是一种特殊的函数,用来在不修改原函数代码的情况下,给函数或方法增加额外功能
#装饰器本质上是一个高阶函数,它接收一个函数作为参数,并返回一个新的函数

#基本结构
"""
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # 在调用原函数之前的操作
        print("Something is happening before the function is called.")
        
        # 调用原函数
        result = func(*args, **kwargs)
        
        # 在调用原函数之后的操作
        print("Something is happening after the function is called.")
        return result
    return wrapper

#使用
@my_decorator  #等价于 say_hello = my_decorator(say_hello),@是语法糖
def say_hello():
    print("Hello, world!")
say_hello()
"""
############带参装饰器
"""
def greet_decorator(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}, {func.__name__} is being called.")
            result = func(*args, **kwargs)
            print(f"{prefix}, {func.__name__} has finished.")
            return result
        return wrapper
    return decorator

@greet_decorator("Hi Tarik") # 等价于 say_morning = greet_decorator("Hi Tarik")(say_morning)
def say_morning():
    print("Good morning!")

say_morning()
"""
########################functools.wraps 保留原函数信息
#在装饰器中,原函数的 __name__ 和 __doc__ 等信息会被替换为装饰器函数的名称
#为了保留原函数的信息,可以使用 functools.wraps 装饰 wrapper
#实现就是原函数__doc__和__name__的copy
"""
import functools
def my_decorator(func):
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        
        # 调用原函数
        result = func(*args, **kwargs)
        
        # 在调用原函数之后的操作
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello():
    """This is the say_hello function.""" # type: ignore
    print("Hello, world!")

print(say_hello.__name__,say_hello.__doc__,sep='\n') 

"""
#######################################################################
#常用示例1:计算函数执行时间
"""
import time
import functools
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Executed {func.__name__} in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Function finished")

slow_function()
"""
####################################################################
"""
#示例 2:检查用户权限
import functools
def requires_permission(user_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if user_role != "admin":
                print("Permission denied")
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator

@requires_permission("user")
def access_sensitive_data():
    print("Accessing sensitive data")

access_sensitive_data()  # 输出:Permission denied

@requires_permission("admin")
def access_sensitive_data_admin():
    print("Accessing sensitive data")

access_sensitive_data_admin()  # 输出:Accessing sensitive data
"""
##################################################################
#类装饰器
#除了函数,装饰器也可以用在类上,给类增加功能通过装饰器,类可以变得更加灵活
"""
def add_methods(cls):
    cls.greet = lambda self: print("Hello from", self.__class__.__name__)
    return cls

@add_methods
class MyClass:
    pass

obj = MyClass()
obj.greet()  # 输出:Hello from MyClass

"""

###################################################################
#functools模块
#functools.wraps:用于保留装饰器包装的原函数信息
#functools.partial:部分应用函数,将部分参数固定
#functools.lru_cache:LRU 缓存装饰器,提高函数多次调用时的性能
#functools.reduce:对可迭代对象进行累积操作
#functools.singledispatch:实现泛型函数,支持不同类型参数
#functools.total_ordering:自动生成类的全部比较方法
#functools.cache:无大小限制的缓存装饰器
#functools.cached_property:缓存类属性,适合惰性求值

#wraps 是一个装饰器,通常用于装饰器内部,用来保留被装饰函数的元数据(如函数名、文档字符串等)使被装饰的函数看起来更像原始函数
#示例见上面例子


#partial 用于将函数的某些参数固定,返回一个新的函数对象
#这个新函数可以调用时传入剩余的参数,相当于部分应用函数
#常用于需要多次传递相同参数的函数,或需要缩减参数数量的场景
"""
from functools import partial

def power(base, exponent):
    return base ** exponent

# 创建一个新函数,将 base 固定为 2
square = partial(power, base=2)
print(square(3))  # 输出:8,相当于 2^3

# 也可以在调用时指定 exponent
cube = partial(power, 2, exponent=3)
print(cube())  # 输出:8
"""

########################################################################
#函数注解（Function Annotations）是一种用于对函数的参数和返回值进行说明的方式
#注解只是提示，并不会限制传入参数的实际类型
#基本语法：
"""
def function_name(param1: annotation1, param2: annotation2) -> return_annotation:
    #函数体
    pass
"""
"""
#示例
def greet(name:str, age: int) -> str:
    return f"hello, {name}. your age is {age} years old"
print(greet('Tarik',27))
#-> str 表示函数返回值应该是字符串类型
#使用 __annotations__ 访问注解
print(greet.__annotations__)

#使用复杂类型注解,  typing 模块来定义复杂的数据类型
from typing import List, Dict, Tuple, Optional

def process_data(data: List[int]) -> Dict[str, int]:
    return {"sum": sum(data), "count": len(data)}

def find_person(name: str) -> Optional[Dict[str, str]]:
    people = {"Alice": {"age": "25"}, "Bob": {"age": "30"}}
    return people.get(name, None)

#typing 模块中的泛型（如 Any、Union、Callable 等）来定义更灵活的类型
from typing import Union, Callable

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y

def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

print(add(10, 5.5))  # 输出：15.5
print(apply_function(lambda x, y: x * y, 2, 3))  # 输出：6

"""
########################################################################
#inspect 模块是 Python 标准库中的一个非常有用的工具，用于获取活动对象的源代码、函数签名、参数等信息
#它主要用于调试、单元测试、自动生成文档和动态分析代码结构

#获取函数签名：检查函数的参数、默认值等。
#获取源代码：获取函数或类的源代码。
#获取对象信息：检测对象的类型、是否是类/函数/方法等。
#检查类继承结构。
#获取当前调用堆栈
"""
import inspect

def example_func(a, b: int, c: str = "default") -> bool:
    return str(a) == c

# 获取函数签名
sig = inspect.signature(example_func)
print(sig)  # 输出： (a, b: int, c: str = 'default') -> bool

# 遍历参数信息
for name, param in sig.parameters.items():
    print(f"参数名称：{name}, 类型：{param.annotation}, 默认值：{param.default}")
"""

######################################################################
