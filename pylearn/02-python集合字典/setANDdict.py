########################################################################
"""
# #set 是一种无序且不重复的集合数据类型set 常用于需要去重操作或进行集合操作(如交集、并集、差集等)的场景

# 创建空集合(只能用 set(),{} 是空字典) set(iterable)
# set元素不可以索引,可以被迭代
s1 = set()
s2 = set([1,2,3,4,5])
s3 = set('hello')
s4 = {1,2,3,4,5}  #用此方式,元素必须可hash ,不可hash类型:list,set
print(s1, s2, s3, s4)

#添加元素
#add(element):添加单个元素如果元素已存在,不会重复添加
#update(iterable):可以添加多个元素,参数是可迭代对象(如列表、元组等)
s = {1,2,3}
s.add(4)
s.update([5,6,7])
print(s)

#删除元素
#remove(element):删除指定元素,如果元素不存在会抛出 KeyError
#discard(element):删除指定元素,如果元素不存在不会报错
#pop():随机删除集合中的一个元素,返回该元素；如果集合为空,抛出 KeyError
#clear():清空集合中的所有元素
s = {1, 2, 3, 4, 5, 6, 7}
s.remove(7)
s.discard(8)
s.pop()
print(s)

# 集合的运算
#并集 ==> 使用 | 运算符或 union() 方法
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1.union(s2)
print(s3, s4)

#交集 ==> 使用 & 运算符或 intersection() 方法
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 & s2
s4 = s1.intersection(s2)
print(s3, s4)

#差集 ==> 使用 - 运算符或 difference() 方法
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 - s2
s4 = s1.difference(s2)
s5 = s2 - s1
print(s3, s4, s5)

# 集合对称差 ==> 使用 ^ 运算符或 symmetric_difference() 方法,得到不属于两者交集的元素
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 ^ s2
s4 = s1.symmetric_difference(s2)
s5 = s2 ^ s1
print(s3, s4, s5)

# 集合比较
#==:判断两个集合是否相等
#<= 或 issubset():判断一个集合是否是另一个集合的子集
#>= 或 issuperset():判断一个集合是否是另一个集合的超集
s1 = {1, 2}
s2 = {1, 2, 3}
s3 = {1, 2}

print(s1 == s3)           # True
print(s1 <= s2)           # True, s1 是 s2 的子集
print(s2 >= s1)           # True, s2 是 s1 的超集
print(s1.issubset(s2))    # True
print(s2.issuperset(s1))  # True

#常见应用
#去重
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)  # {1, 2, 3, 4, 5}
#过滤
#判断元素是否存在:集合的成员测试操作(in)速度比列表快,因为 set 是基于哈希表的
s = {1, 2, 3, 4, 5}
print(3 in s)  # True
print(6 in s)  # False

# 集合推导式
squared_set = {x ** 2 for x in range(10) if x % 2 == 0}  # {0, 4, 16, 36, 64}
"""
########################################################################
#随机产生2组各10个数字的列表,要求:
#1. 每个数字的取值范围[10,20]
#统计20个数字中,一共有不同数字
"""
import random
def generate_random_list():
    list1 = random.sample(range(10, 21), 10)
    list2 = random.sample(range(10, 21), 10)
    return list1, list2

list1, list2 = generate_random_list()

# 1. 统计20个数字中,一共有不同数字

def count_unique_numbers(list1, list2):
    total_numbers = list1 + list2
    unique_numbers = set(total_numbers)
    return len(unique_numbers)

count = count_unique_numbers(list1, list2)

print(f"There are {count} unique numbers in total.")
"""

################################################################
"""
#冒泡排序:冒泡排序通过反复交换相邻的元素,将较大的元素逐步“冒泡”到列表的末尾这个过程会多次遍历列表,直到整个列表有序
#时间复杂度为O(n^2)适用于小规模数据集
#算法步骤
#从第一个元素开始,比较相邻的两个元素如果前一个元素比后一个元素大,就交换它们
#对列表进行多次遍历,每次遍历会将最大的元素“冒泡”到未排序部分的末尾
#重复步骤1和2,直到没有任何元素需要交换,表明列表已经有序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 优化:如果在一轮排序中没有发生交换,说明列表已排序完毕
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果没有元素交换,提前结束排序
        if not swapped:
            break
    return arr

################################################################
#选择排序:时间复杂度为O(n^2)
#从列表中找到最小的元素,将它放在列表的起始位置
#从剩下的未排序部分中找到最小的元素,将它放在已排序部分的末尾
#重复步骤1和2,直到所有元素都被排序

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 假设当前元素是未排序部分中的最小值
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 将找到的最小值交换到已排序部分的末尾
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
"""

##################################################################
"""
#dict 是一种基于哈希表的数据结构,用于存储键-值对。
#dict 是无序的(Python 3.7 之后字典保持插入顺序),可以通过键来快速访问对应的值,键必须是唯一且不可变的
# 使用大括号 {}
d1 = {"name": "Tarik", "age": 30}

# 使用 dict() 函数
d2 = dict(name="Bob", age=30)

# 使用键值对列表
d3 = dict([("name", "Charlie"), ("age", 28)])

# 空字典
d4 = {}


#访问元素
d = {"name": "Alice", "age": 25}
print(d["name"])  # 输出: Alice

#增加和修改元素
d["city"] = "New York"  # 添加新键值对
d["age"] = 26           # 修改已有键的值

#删除元素
#del 删除指定键值对,若键不存在会引发 KeyError。
#pop(key) 删除并返回指定键的值,若键不存在可指定默认返回值。
#popitem() 随机删除并返回键值对(Python 3.7 后返回最后插入的项)。
#clear() 清空字典。
d = {"name": "Alice", "age": 25}
del d["name"]
d.pop("age", None)
d.clear()  # 清空字典

#常用方法
#获取值 get(key, default):获取指定键的值,若键不存在则返回 default
d = {"name": "Alice", "age": 25}
print(d.get("age", 0))       # 输出: 25
print(d.get("height", 160))   # 输出: 160 (默认值)

# 获取键、值、键值对
#keys():返回所有键的视图。
#values():返回所有值的视图。
#items():返回所有键值对的视图(每对元素为一个元组)
d = {"name": "Alice", "age": 25}
print(list(d.keys()))    # 输出: ['name', 'age']    
print(list(d.values()))  # 输出: ['Alice', 25]
print(list(d.items()))   # 输出: [('name', 'Alice'), ('age', 25)]
#以上例子不转list会返回一个迭代器对象

#更新字典
#update(other_dict):用其他字典或键值对更新当前字典
d = {"name": "Alice", "age": 25}
d.update({"city": "New York", "age": 26})
# d 现在为: {'name': 'Alice', 'age': 26, 'city': 'New York'}


#设置默认值
#setdefault(key, default):若键存在则返回对应值,否则插入 default 值并返回
d = {"name": "Alice"}
d.setdefault("age", 25)  # age 不存在,设置为 25
print(d)  # 输出: {'name': 'Alice', 'age': 25}

#字典推导式
squared_dict = {x: x ** 2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
filtered_dict = {k: v for k, v in d.items() if v > 20}


#字典遍历
d = {"name": "Alice", "age": 25}
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

#单独遍历key
for key in d.keys():
    print(key)

#单独遍历value
for value in d.values():
    print(value)

#字典嵌套
students = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 30, "city": "Los Angeles"}
}
print(students["Alice"]["city"])  # 输出: New York
"""

################################################################
"""
#defaultdict是 Python 的 collections 模块中的一种字典类型,
#它可以为字典中的键提供默认值,避免了访问不存在的键时抛出 KeyError 异常
from collections import defaultdict

# 创建一个 defaultdict,默认值为整数0
d = defaultdict(int)

d["a"] += 1  # 若 "a" 不存在,则会自动初始化为 0,然后执行 d["a"] += 1
print(d)     # 输出: defaultdict(<class 'int'>, {'a': 1})

##工厂函数的作用
#int:返回 0,适合做计数。
#list:返回空列表 [],适合收集多个值。
#set:返回空集合 set(),适合去重收集多个值。
#lambda 表达式:自定义任意默认值

#计数示例
from collections import defaultdict

text = "hello world"
char_count = defaultdict(int)
for char in text:
    char_count[char] += 1

print(char_count)  # 输出: defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


#list 示例  当需要将多个值收集到同一个键下时,可以使用 list 作为默认值工厂
from collections import defaultdict

data = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
d = defaultdict(list)
for key, value in data:
    d[key].append(value)

print(d)  # 输出: defaultdict(<class 'list'>, {'a': [1, 3], 'b': [2, 4]})

#如果不需要为新键自动生成默认值,dict 更为合适；
#但在需要默认初始化的场景下,defaultdict 提供了更简洁的实现方式
"""
##################################################################
"""
#OrderedDict 是 Python collections 模块中的一种字典类型
#它在 Python 3.6 之前用于维护字典中元素的插入顺序
#在 Python 3.7 及之后,普通字典已经默认按照插入顺序存储元素
#因此在大多数情况下,普通字典和 OrderedDict 的行为是相同的
#然而,OrderedDict 仍然有一些独特的特性和用途

#OrderedDict 的 popitem 和 move_to_end 操作可以实现最近最少使用(LRU)缓存,比如在缓存中删除最早访问的数据

#示例:使用 OrderedDict 实现简单的 LRU 缓存
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        # 将被访问的键移到末尾
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # 更新值并将键移到末尾
            self.cache.move_to_end(key)
        self.cache[key] = value
        # 超出容量时,删除最前面的键值对
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# 示例
lru_cache = LRUCache(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))  # 输出: 1
lru_cache.put(3, 3)      # 删除键 2
print(lru_cache.get(2))  # 输出: -1 (键 2 已被移除)
"""

################################################################
"""
#用户输入一个数字：升序打印每一位数字及其重复的次数

#分析：结果类似{"1":3,"2":1,"7":2} 
#输入为数字，需要转字符串后迭代并统计每个数字的次数 
#拿到字典后对key进行排序打印
user_input = input("pls input an number: ")
str_num = str(user_input)
result = {}
for stn in str_num:
    if stn in result:
        result[stn] += 1
    else:
        result[stn] = 1
print(result)

for key in sorted(result.keys()):
    print(f"{key} 出现 {result[key]} 次")

################################################################
#数字重复统计：随机产生100个整数，范围[-1000,1000]，升序输出所有不同的数字机器重复的次数

import random
lst = []
for i in range(101):
    num = random.randint(-1000, 1001)
    lst.append(num)
result = {}
for num in lst:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1
print(result)

for key in sorted(result.keys()):
    print(f"{key} 出现 {result[key]} 次")


################################################################
#字符串统计：字符表'abcdefghigklmnopqrstuvwxyz'中随机挑选2个字母组成字符串
#共挑选100个，降序输出这100个字符串及其重复次数
import random
lst = []
initstr = 'abcdefghigklmnopqrstuvwxyz'
for i in range(101):
    str1 = random.choice(initstr)
    str2 = random.choice(initstr)
    finstr = str1 + str2
    lst.append(finstr)
print(lst)
result = {}
for key in sorted(lst,reverse=True):
    if key in result:
        result[key] += 1
    else:
        result[key] =1

print(result)

"""

################################################################
"""
#datetime 是 Python 的一个标准模块
#用于处理日期和时间数据，提供了日期、时间、日期时间以及时间差的相关操作
#datetime 模块中包含几个重要的类：datetime、date、time、timedelta 和 timezone
from datetime import datetime, date, time, timedelta, timezone

#################datetime 类
# 使用当前日期和时间
now = datetime.now()
print("当前日期和时间：", now)

# 使用指定的日期和时间
dt = datetime(2023, 11, 7, 15, 30, 0)
print("指定的日期和时间：", dt)

#常用方法
#now()：返回当前日期和时间
#today()：返回当前本地日期和时间
#strftime(format)：将 datetime 对象格式化为字符串
#strptime(date_string, format)：将字符串转换为 datetime 对象，需指定格式
# 格式化 datetime 对象
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化日期和时间：", formatted)

# 将字符串转换为 datetime 对象
date_str = "2023-11-07 15:30:00"
dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("解析的 datetime 对象：", dt_obj)
#----------------------------------------------------------------

#################date 类
#date 类仅表示日期部分，包括年、月、日
# 获取当前日期
from datetime import datetime, date, time, timedelta, timezone
today = date.today()
print("当前日期：", today)

# 使用指定的日期
d = date(2023, 11, 7)
print("指定的日期：", d)

#常用方法
#today()：返回当前日期
#strftime(format)：将 date 对象格式化为字符串
#fromisoformat(date_string)：将 ISO 格式的字符串转换为 date 对象
#replace(year, month, day)：返回修改后的新日期对象

# 格式化 date 对象
formatted_date = today.strftime("%Y-%m-%d")
print("格式化日期：", formatted_date)

# 从字符串转换为 date 对象
iso_date = date.fromisoformat("2023-11-07")
print("ISO 格式的日期：", iso_date)

#----------------------------------------------------------------
################################time 类
# 使用指定的时间
t = time(15, 30, 0)
print("指定的时间：", t)

#常用方法
#strftime(format)：将 time 对象格式化为字符串
#replace(hour, minute, second, microsecond)：返回修改后的新时间对象

# 格式化 time 对象
formatted_time = t.strftime("%H:%M:%S")
print("格式化时间：", formatted_time)


#------------------------------------------------------------
#########timedelta 类
# 创建一个时间间隔
delta = timedelta(days=5, hours=3, minutes=30)
print("时间间隔：", delta)

# 当前日期加上时间间隔
future_date = today + delta
print("未来日期：", future_date)

# 计算两个日期之间的差
date1 = date(2023, 11, 7)
date2 = date(2023, 12, 1)
difference = date2 - date1
print("日期差：", difference.days, "天")


#------------------------------------------------------------
#########timezone 类
# 创建带时区的 datetime 对象
from datetime import datetime, date, time, timedelta, timezone
dt_with_timezone = datetime(2023, 11, 7, 15, 30, tzinfo=timezone.utc)
print("带时区的 datetime：", dt_with_timezone)

#常用方法
#astimezone(tz)：将带时区的 datetime 对象转换为另一个时区
#utcnow()：获取当前 UTC 时间

# 将 UTC 时间转换为本地时间
local_time = dt_with_timezone.astimezone()
print("本地时间：", local_time)
"""

################################################################
"""
#列表解析式：对列表中的元素进行操作并生成新列表
#语法：[表达式 for 变量 in 可迭代对象 if 条件]

# 使用 for 循环生成平方数
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 使用列表解析式生成平方数
squares = [i ** 2 for i in range(10)]
print(squares)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#嵌套的列表解析式：[表达式 for 变量1 in 可迭代对象1 for 变量2 in 可迭代对象2]
cartesian_product = [(x, y) for x in [1, 2] for y in [3, 4]]
print(cartesian_product)  # 输出: [(1, 3), (1, 4), (2, 3), (2, 4)]

#带条件判断的嵌套列表解析式
unique_pairs = [(x, y) for x in [1, 2, 3] for y in [1, 2, 3] if x != y]
print(unique_pairs)  # 输出: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 使用 if ... else 的条件表达式:[表达式1 if 条件 else 表达式2 for 变量 in 可迭代对象]
result = [x if x % 2 != 0 else -x for x in range(1, 6)]
print(result)  # 输出: [1, -2, 3, -4, 5]

##列表解析式生成一个九九乘法表
# 使用列表解析式生成九九乘法表
# 使用列表解析式生成九九乘法表并按三角形格式打印
for i in range(1, 10):
    # 每一行显示从 1 到当前行的乘法表达式
    row = [f"{i} * {j} = {i * j}" for j in range(1, i + 1)]
    # 使用制表符连接每一行的表达式
    print("\t".join(row))
"""

################################################################
"""
#生成器表达式（Generator Expressions）是 Python 提供的一种创建生成器（generator）对象的简洁方法
# 与列表解析式类似，但其返回的是一个生成器对象，而不是一个列表
# 生成器对象是惰性计算的，这意味着它只在需要时才生成数据，具有更高的内存效率，尤其是在处理大量数据时

#(表达式 for 变量 in 可迭代对象 if 条件)    #列表解析式为[],生成器表达式为()

gen = (x**2 for x in range(1, 6))

# 使用 next() 来获取生成器中的下一个元素
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 4
print(next(gen))  # 输出: 9

#for循环遍历
gen = (x**2 for x in range(1, 6))
for val in gen:
    print(val)

#生成器的惰性求值
# 列表解析式会立即计算并返回列表
list_comp = [x**2 for x in range(1, 6)]
print(list_comp)  # 输出: [1, 4, 9, 16, 25]

# 生成器表达式返回的是生成器对象，值只有在需要时才会被计算出来
gen_exp = (x**2 for x in range(1, 6))
print(gen_exp)  # 输出: <generator object <genexpr> at 0x...>
#使用next获取下一个值
gen = (x**2 for x in range(1, 6))
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 4

#与 list() 和 for 循环结合
gen = (x**2 for x in range(1, 6))
squared_list = list(gen)
print(squared_list)  # 输出: [1, 4, 9, 16, 25]

gen = (x**2 for x in range(1, 6))
for value in gen:
    print(value)
"""
###################################################################
"""
#集合解析式和字典解析式

#集合解析式
#{表达式 for 变量 in 可迭代对象 if 条件}
squares = {x**2 for x in range(1, 6)}
print(squares)  # 输出: {1, 4, 9, 16, 25}


#字典解析式
{键: 值 for 变量 in 可迭代对象 if 条件}
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # 输出: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""
################################################################