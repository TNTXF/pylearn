#class from P36 to P53, current is ===> P46

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
#给定一个不超过5位的正整数，判断其有几位，依次打印每位的数字
#vs code乱码解决：新建一个环境变量，key=PYTHONIOENCODING  value=UTF-8
'''
def print_digits(number: int):
    if 1 <= number <= 99999:
        number_str = str(number)
        digit_count = len(number_str)
        print(f"这个数有 {digit_count} 位")
        
        for i, digit in enumerate(number_str, 1):
            print(f"第 {i} 位：{digit}")
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
#给定一个数，求它的阶乘的和
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
#给定一个数，求它的阶乘的和，如5，结果为153（1+2+6+24+120）
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
#给定一个数，判断它是否为质数
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
            #:2 是格式化指令，表示将结果右对齐并保留 2 个字符的宽度
            # end="\t" print 函数的 end 参数指定打印结尾的字符。
            # 默认情况下,print 在结尾会自动换行，
            # 但这里用 "\t" 替换了换行符，意思是每次打印后不换行，
            # 而是用制表符 (\t) 隔开输出内容，使每一列在一行中对齐
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
print(lst) #就地修改，对当前lst进行修改，时间复杂度O(1)

lst = [i for i in range(10) if i % 2 == 0]
print(lst.insert(3,5)) # return None
print(lst) # 就地修改，对当前lst进行修改，时间复杂度O(n)

lst = [i for i in range(10) if i % 2 == 0]
lst.extend([1,2,3,4,5])
print(lst) # 就地修改，对当前lst进行修改

lst1 = [i for i in range(10) if i % 2 == 0]
lst2=[1,2,3,4,5]
lst = lst1 + lst2 # 新创建一个列表
print(lst)

lst = [i for i in range(10) if i % 2 == 0]
lst1 = lst*2
print(lst1) 

lst = [i for i in range(10) if i % 2 == 0]
print(lst.remove(2)) # return None
print(lst) # 就地修改，对当前lst进行修改

lst = [i for i in range(10) if i % 2 == 0]
lst.pop(2) #pop([index])
print(lst.pop()) # return item of index
print(lst) # 就地修改，对当前lst进行修改


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

#嵌套列表，引用类型copy
lst0 = [1,[2,3],4]  #[2,3]这里存储的是地址引用
lst1 = lst0.copy()
lst1[1][0] = 10
print(lst0 == lst1) # return True
print(lst0 is lst1) # return False

#copy()是浅拷贝，浅拷贝创建一个新对象，但不递归地复制内部的子对象。
#因此，浅拷贝后的新对象包含的子对象仍然是对原始对象中子对象的引用

import copy
lst0 = [1,[2,3],4]  #[2,3]这里存储的是地址引用
lst1 = copy.deepcopy(lst0)
lst1[1][0] = 10
print(lst0 == lst1) # return False
print(lst0 is lst1) # return False
#deepcopy()深拷贝会递归地复制对象及其所有子对象，创建一个全新的对象及其所有嵌套对象的副本
"""

########################################################################
#求100以内的素数
"""
def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):  # 从 2 开始，因为 1 不是素数
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

#tuple()  创建一个空元组,基本没用，因为tuple不可变
#tuple(iterable)  创建一个元组，iterable 必须是可迭代的

t = ()
t = tuple()
t = tuple(range(10))

t = tuple(1,)
t = (1,) * 5
t = (1,2,3) * 5
print(t)

