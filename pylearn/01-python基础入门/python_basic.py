

#位运算取反的结果是 -(x + 1), such as:  print(~12) ==> -13
#print(~12)  # -13

########################################################################
#practice one: 给定一个5位之内的数,判断有几位
"""
while True:
    try:
        num = int(input("Enter a integer number: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        continue
    if  0 <= num <= 99999:
        if num/10000 >1:
            print("5 bit integer")
        elif num/1000 >1:
            print("4 bit integer")

        elif num/100 >1:
            print("3 bit integer")
        elif num/10 >1:
            print("2 bit integer")
        else :
            print("1 bit integer")
        break
"""
########################################################################


#print(list(range(10, 0,-1)))

#for loop
'''
for i in range(10):
    if not i%2:
        print(i)
'''

'''
count = 0
for i in range(0,1000,7):
    print(i)
    count += 1
    if count >= 20:
        print(count)
        break
'''
########################################################################
#给定一个不超过5位的正整数,判断其有几位,依次打印每位的数字
#vs code乱码解决:新建一个环境变量,key=PYTHONIOENCODING  value=UTF-8
'''
def print_digits(number: int):
    if 1 <= number <= 99999:
        number_str = str(number)
        digit_count = len(number_str)
        print(f"这个数有 {digit_count} 位")
        
        for i, digit in enumerate(number_str, 1):
            print(f"第 {i} 位:{digit}")
    else:
        print("please enter a number that is between 1 and 99999")

print_digits(12385)
'''

########################################################################
#打印一个正方形
"""
def print_square(size):
    if size <= 0:
        print("请输入一个正整数作为边长")
        return
    for i in range(size):
        print('*' * size)

print_square(2)
"""

########################################################################
#求100以内所有奇数的和,下面代码可以改进
"""
def sum_of_odd_numbers(n: int):
    sum = 0
    for i in range(1,n+1):
        if i%2 != 0:
            sum += i
    return sum

print(sum_of_odd_numbers(100))
"""
########################################################################
#给定一个数,求它的阶乘的和
"""
def factorial(n: int):
    if n < 0:
        return r"Error: 请输入正数"
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(-5))
"""

########################################################################
#给定一个数,求它的阶乘的和,如5,结果为153(1+2+6+24+120)
"""
def factorial_sum(n):
    factorial = 1  
    total_sum = 0 

    for i in range(1, n + 1):
        factorial *= i 
        total_sum += factorial 

    return total_sum

result = factorial_sum(5)
print(result)  
"""
########################################################################
#给定一个数,判断它是否为质数
"""
def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False    
    return True
print(is_prime(100000)) 
"""
########################################################################
#打印一个九九乘法表
"""
def print_multiplication_table(n: int):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(f"{i} x {j} = {i*j:2}", end="\t")
            #:2 是格式化指令,表示将结果右对齐并保留 2 个字符的宽度
            # end="\t" print 函数的 end 参数指定打印结尾的字符。
            # 默认情况下,print 在结尾会自动换行,
            # 但这里用 "\t" 替换了换行符,意思是每次打印后不换行,
            # 而是用制表符 (\t) 隔开输出内容,使每一列在一行中对齐
        print()

print_multiplication_table(9)
"""
########################################################################
#用*号打印一个菱形
'''
def print_diamond(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

print_diamond(3)
'''
########################################################################
#100以内的斐波那契数列
'''
def fibonacci(n:int):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

print(fibonacci(100)[-1])
'''
########################################################################
"""
import math
print(round(4.6))  # 5
print(round(4.5))   # 4
print(round(5.5)) # 6
#round() 四舍六入五取偶

print(math.ceil(4.6))  # 5
print(math.ceil(4.5))  # 5

print(math.floor(4.6))  # 4
print(math.floor(4.5))  # 4
print(math.sqrt(25))  # 5.0
"""
#type(object) 获取对象的类型, isinstance(object, class) 判断是否是特定类的实例
#type('ab')
#isinstance('ab', str)

########################################################################
#--------------------------------list----------------------------------#
"""
help(list)
lst = list()
lst = []
lst = [1, 2, 3, 'ab']
lst = [i for i in range(10) if i % 2 == 0]
print(lst[0])
print(lst)

lst = [i for i in range(10) if i % 2 == 0]
print(lst.index(2,0,3)) # index(value,[start,[stop]]) , 索引范围 [0, 3) 内寻找值 6 的位置
#result ==> ValueError: 6 is not in list
import sys
print(sys.getsizeof(lst))  
print(sys.getsizeof([0,2,4,6,8])) 
print(sys.getsizeof([0]*5))  # 
#为什么三个列表在内存中的大小不一样？

lst = [i for i in range(10) if i % 2 == 0]
print(lst.append(5))   # return None
print(lst) #就地修改,对当前lst进行修改,时间复杂度O(1)

lst = [i for i in range(10) if i % 2 == 0]
print(lst.insert(3,5)) # return None
print(lst) # 就地修改,对当前lst进行修改,时间复杂度O(n)

lst = [i for i in range(10) if i % 2 == 0]
lst.extend([1,2,3,4,5])
print(lst) # 就地修改,对当前lst进行修改

lst1 = [i for i in range(10) if i % 2 == 0]
lst2=[1,2,3,4,5]
lst = lst1 + lst2 # 新创建一个列表
print(lst)

lst = [i for i in range(10) if i % 2 == 0]
lst1 = lst*2
print(lst1) 

lst = [i for i in range(10) if i % 2 == 0]
print(lst.remove(2)) # return None
print(lst) # 就地修改,对当前lst进行修改

lst = [i for i in range(10) if i % 2 == 0]
lst.pop(2) #pop([index])
print(lst.pop()) # return item of index
print(lst) # 就地修改,对当前lst进行修改


lst = [i for i in range(10) if i % 2 == 0]
lst.clear() # remove all items

lst = [i for i in range(10) if i % 2 == 0]
lst.reverse() # return None
print(lst) #就地修改,反转列表

lst = [1, 0, 3, 2, 4,'a']
#lst.sort() # return None
lst.sort(key=str, reverse=True) #
print(lst) #sort(key=None, reverse=False) #default

a = [3,4] in [1,2,[3,4]]  # in and not in
print(a) # return True

#列表复制
lst0 = list(range(4))
lst1 = list(range(4))
print(lst0 == lst1) # return True
print(lst0 is lst1) # return False
print('-------')
lst2 = lst0
print(id(lst2) == id(lst0)) # return True
print(lst2 is lst0) # return True
print('-------')
lst2[2] = 10
print(lst2 == lst0) # return True
print(lst2 is lst0) # return True
print(lst2,'|',lst0)  #[0, 1, 10, 3] | [0, 1, 10, 3]
print('-------')
lst3 = lst2.copy()  # create a new list
print(lst3 == lst2) # return True
print(lst3 is lst2) # return False

#嵌套列表,引用类型copy
lst0 = [1,[2,3],4]  #[2,3]这里存储的是地址引用
lst1 = lst0.copy()
lst1[1][0] = 10
print(lst0 == lst1) # return True
print(lst0 is lst1) # return False

#copy()是浅拷贝,浅拷贝创建一个新对象,但不递归地复制内部的子对象。
#因此,浅拷贝后的新对象包含的子对象仍然是对原始对象中子对象的引用

import copy
lst0 = [1,[2,3],4]  #[2,3]这里存储的是地址引用
lst1 = copy.deepcopy(lst0)
lst1[1][0] = 10
print(lst0 == lst1) # return False
print(lst0 is lst1) # return False
#deepcopy()深拷贝会递归地复制对象及其所有子对象,创建一个全新的对象及其所有嵌套对象的副本
"""

########################################################################
#求100以内的素数
"""
def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):  # 从 2 开始,因为 1 不是素数
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # 只需检查到 sqrt(num)
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(find_primes(100))
"""
##########################################################################
#-------------------------------tuple------------------------------------#
"""
#tuple()  创建一个空元组,基本没用,因为tuple不可变
#tuple(iterable)  创建一个元组,iterable 必须是可迭代的

t = ()
t = tuple()
t = tuple(range(10))

t = tuple(1,)
t = (1,) * 5
t = (1,2,3) * 5
print(t)

#tuple[index] 获取元素
t = (1,2,3) * 5
print(t.index(2,0,5))
print(t.count(2))
print(len(t))

#元组是只读的,没有列表那么多方法

#命名元组,namedtuple('name', ['attr1', 'attr2'])
#Python 中的 命名元组(namedtuple)是 collections 模块提供的一种数据结构,用于创建简单的类。
#这种结构类似于普通的元组,但支持用名称来访问字段,从而提高了代码的可读性和可维护性
################################
from collections import namedtuple
# 创建一个命名元组类型 Point,包含 x 和 y 两个字段
Point = namedtuple('Point', ['x', 'y'])
# 实例化一个 Point 对象
p = Point(3, 4)
# 访问字段值
print(p.x)  # 输出 3
print(p.y)  # 输出 4

#命名元组的特点:
#不可变性:命名元组是不可变的,就像普通元组一样,一旦创建就不能修改字段的值。
#字段名访问:可以通过字段名(例如 p.x)访问数据,而不必使用索引(如 p[0])。
#可读性强:命名元组的代码可读性比普通元组更好,因为字段有明确的名字
# 使用 _replace() 替换字段值
p2 = p._replace(x=10)
print(p2)  # 输出 Point(x=10, y=4)
# 使用 _asdict() 转换为字典
print(p._asdict())  # 输出 OrderedDict([('x', 3), ('y', 4)])
# 使用 _fields 查看字段名
print(Point._fields)  # 输出 ('x', 'y')
# 序列解包
x, y = p
print(x, y)  # 输出 3 4
"""
################################################################
#字符串:一个个字符组成的有序序列,不可变对象
"""
s1 = 'hello'
s2 = "hello"
s4 = 'hello\n world'
s5 = r"hello\n world"
s6 = 'C:\windows\nt'
s7 = R"C:\windows\nt"
s8 = 'C:\windows\\nt'

for c in s8:
    print(c)
    print(type(c))

lst = list(s8)  #可迭代

s = s1 + s2
print(s)

#separator.join(iterable)
a = 'abc'
print(".".join(a))  # output ==>a.b.c

numbers = ["1", "2", "3", "4"]
result = ",".join(numbers)
print(result)  # 输出: "1,2,3,4"

#字符串分割 split和partition

#str.split(sep=None, maxsplit=-1)  
#rsplit() 的功能类似于 split(),但从右侧开始分割。
#sep:分隔符,默认为 None,表示按任意空白字符(空格、换行、制表符等)分割。
#maxsplit:最大分割次数,默认为 -1,表示分割所有匹配项。
text = "apple,orange,banana"
result = text.split(',')
print(result)

text = "Python is fun"
result = text.split(maxsplit=1)
print(result)  

#splitlines() 根据行分隔符(\n、\r\n)分割字符串,适用于处理多行文本
#str.splitlines(keepends=False)   #keepends:是否保留行分隔符,默认为 False
text = "Hello\nWorld\nPython"
result = text.splitlines()
print(result)  # 输出: ['Hello', 'World', 'Python']


#partition() 将字符串分成三部分:指定分隔符之前的部分、分隔符本身、分隔符之后的部分。
#rpartition() 从右侧开始分割,其他与 partition() 相同
#str.partition(sep)
#str.rpartition(sep)

text = "apple-banana-orange"
result = text.partition("-")
print(result)  # 输出: ('apple', '-', 'banana-orange')

#re.split() 是正则表达式的分割方法,适合复杂的分割模式
import re
text = "apple1banana2orange3"
result = re.split(r'\d', text)
#前缀 r 表示这是一个 原始字符串(raw string)。
#在 Python 中,原始字符串的作用是告诉解释器不要对字符串中的反斜杠(\)进行转义处理
print(result)  # 输出: ['apple', 'banana', 'orange', '']

#字符串其他操作函数
print('I am a student'.upper())
print('I am a student'.lower())
print('I am a student'.swapcase())
print('I am a student'.title())
print('I am a student'.capitalize())
print('I am a student'.center(20))
print('I am a student'.zfill(20))
print('I am a student'.ljust(20))
print('I am a student'.rjust(20))
print('I am a student'.replace('student', 'teacher'))  # 返回新的字符串
# str.count(sub[, start[, end]]) ,同理还有 lstrip(), rstrip()
print('\n \r\n I am a student  \r \n'.strip())    #常用,去掉两端的空格、换行符
print('I am a student'.find('am'))  #str.find(sub[, start[, end]]),未找到返回-1
print('I am a student'.index('am')) #未找到抛异常
print('I am a student'.count('a'))
print('I am a student'.startswith('I am'))
print('I am a student'.endswith('student'))
#字符串is系列判断
a = 'abc123Ads'
a.isalnum()
a.isalpha()
a.isdecimal()
a.isdigit()
a.isidentifier()
a.islower()
a.isupper()
a.isspace()
"""
##################
"""
# 字符串格式化方式一: % 操作符
#%s:字符串
#%d:整数
#%f:浮点数(默认精度为小数点后 6 位)
name = "Alice"
age = 25
height = 1.75
print("Name: %s, Age: %d, Height: %.2f" % (name, age, height))

# 字符串格式化方式二: str.format()
#"template string with {placeholders}".format(value1, value2, ...)
name = "Alice"
age = 25
height = 1.75

# 使用 { } 占位符
print("Name: {}, Age: {}, Height: {:.2f}".format(name, age, height)) 
print("Name: {n}, Age: {a}, Height: {h:.2f}".format(n=name, a=age, h=height)) #命名参数
print("Name: {0}, Age: {1}, Height: {2:.2f}".format(name, age, height))   #使用索引


# 字符串格式化方式三: f-string
name = "Alice"
age = 25
height = 1.75

print(f"Name: {name}, Age: {age}, Height: {height:.2f}")
#{} 里面的表达式可以是任何 Python 表达式
score = 88
print(f"Next year {name} will be {age + 1} years old and will aim for a score above {score + 5}.")


# 字符串格式化方式四:Template
from string import Template

template = Template("Hello, $name! You are $age years old.")
result = template.substitute(name="Alice", age=25)
print(result)

# %  ==> 旧式格式化字符串  ==>  简单的格式化,不推荐在新代码中使用
# str.format() ==> Python 3 推荐方法  ==>  复杂的格式化场景
# f-string ==> 格式化字符串字面量,简洁高效  ==>  Python 3.6+,适合嵌入表达式和变量
# Template ==> 安全的替换变量,不支持复杂表达式  ==> 需要安全替换、不需要复杂表达式的场景
"""
################################################################
#bytes and bytearray: 字节序列和可变字节序列
"""
#bytes 是不可变的字节序列,类似于字符串。它一旦创建,就无法更改其内容
# 使用 b'' 前缀
b = b"hello"
print(b)  # 输出: b'hello'

# 使用 bytes() 函数
b = bytes([104, 101, 108, 108, 111])
print(b)  # 输出: b'hello'

# 使用字符串的 encode 方法(将字符串编码为 bytes)
s = "hello"
b = s.encode('utf-8')
print(b)  # 输出: b'hello'
#不可变:无法修改 bytes 对象中的任何字节。
#支持切片和迭代:与字符串类似,可以通过索引和切片访问其中的字节
#常用于需要不可变字节数据的场景,例如网络通信、加密数据、文件 I/O 等

#------------
#bytearray 是可变的字节序列,类似于可变字符串。可以修改其中的内容,支持追加、修改、删除等操作
# 使用 bytearray() 函数
b_arr = bytearray([104, 101, 108, 108, 111])
print(b_arr)  # 输出: bytearray(b'hello')

# 将 bytes 转换为 bytearray
b = b"hello"
b_arr = bytearray(b)
print(b_arr)  # 输出: bytearray(b'hello')

#修改
b_arr = bytearray(b"hello")
b_arr[0] = 72  # 修改第一个字节(H 的 ASCII 值为 72)
print(b_arr)  # 输出: bytearray(b'Hello')

b_arr.append(33)  # 添加 '!' 的 ASCII 值
print(b_arr)  # 输出: bytearray(b'Hello!')
"""
################################################################
#python解构，Python 提供了多种解构方式，包括对列表、元组、字典的解构赋值
"""
# 简单的元组解构
person = ("Alice", 30)
name, age = person
print(name)  # 输出: Alice
print(age)   # 输出: 30

# 列表解构
coordinates = [10, 20, 30]
x, y, z = coordinates
print(x, y, z)  # 输出: 10 20 30

#使用*
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)    # 输出: 1
print(middle)   # 输出: [2, 3, 4]
print(last)     # 输出: 5

# 字典解构
# 遍历并解构字典的键值对
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")

# 字典解构传参
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

person = {"name": "Alice", "age": 30}
greet(**person)  # 使用 ** 将字典解构为函数的参数

a,b = 1,2 # 左边是(1,2)元组,右边是解构, a=1, b=2
"""
################################################################
#python丢弃变量
# 单个变量不需要                name, _ = ("Alice", "unused_value")
#多个变量不需要                 first, _, _, last = data
#忽略循环变量                   for _ in range(5):
#忽略函数返回值中的部分值        x, _, z = get_coordinates()
#丢弃不需要的多个中间值          first, *_, last = data

