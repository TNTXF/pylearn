#re 模块用于处理正则表达式,它提供了丰富的正则表达式处理功能，包括模式匹配、搜索、替换等

####常用方法####
"""
#re.match(pattern, string, flags=0)
#从字符串开头开始匹配，若匹配成功，返回 Match 对象
import re
result = re.match(r'hello', 'hello world')
if result:
    print("匹配成功")


#re.search(pattern, string, flags=0)
#在字符串中搜索符合模式的第一个匹配项，不要求从头开始匹配;找到则返回 Match 对象，否则返回 None。
import re
result = re.search(r"world", "hello , world is a good day")
#result => return a Match object if found, else None
print(result) 
if result:
    print("匹配成功")

#re.findall(pattern, string, flags=0)
#返回字符串中所有符合模式的非重叠匹配，结果为一个列表
import re
result = re.findall(r"\d+", "hello 123 world 456")

print(result)

#re.finditer(pattern, string, flags=0)
#与 findall 类似，但返回的是一个迭代器，每个元素都是一个 Match 对象

import re
result = re.finditer(r"\d+", "hello 123 world 456")
for match in result:
    print(match.group())

#re.sub(pattern, repl, string, count=0, flags=0)
#使用 repl 替换字符串中所有符合 pattern 的匹配项，可以指定替换次数 count

import re
result = re.sub(r"\d+", "***", "hello 123 world 456")
print(result)

#re.split(pattern, string, maxsplit=0, flags=0)
#按照匹配的模式分割字符串，返回分割后的列表。maxsplit 限制分割次数
import re
result = re.split(r'\s+', 'I have 2 apples and 3 oranges')
print(result)  # 输出：['I', 'have', '2', 'apples', 'and', '3', 'oranges']

#re.fullmatch(pattern, string, flags=0)
#要求整个字符串完全符合模式匹配，成功则返回 Match 对象，否则返回 None
import re
result = re.fullmatch(r'\d+', '12345')
if result:
    print("完全匹配")
"""

####常用匹配模式####
#. 匹配任意字符（除换行符外）
#\d 匹配数字，等价于 [0-9]
#\D 匹配非数字
#\w 匹配字母、数字、下划线，等价于 [a-zA-Z0-9_]
#\W 匹配非字母、数字、下划线
#\s 匹配空白字符（空格、制表符、换页符等）
#\S 匹配非空白字符
#^ 匹配字符串的开头
#$ 匹配字符串的结尾
#* 匹配前一个字符零次或多次
#+ 匹配前一个字符一次或多次
#? 匹配前一个字符零次或一次
#{n,m} 匹配前一个字符至少 n 次，至多 m 次

####编译正则表达式####
"""
#使用 re.compile() 可以编译正则表达式，返回一个正则表达式对象，可以复用并提升匹配效率
import re
pattern = re.compile(r"\d+")
result = pattern.findall('I have 2 apples and 3 oranges')
print(result)  # 输出：['2', '3']

####捕获与分组####
import re
result = re.search(r'(\d+) apples and (\d+) oranges', 'I have 2 apples and 3 oranges')
if result:
    print(result.group(0))  # 输出：'2 apples and 3 oranges'
    print(result.group(1))  # 输出：2
    print(result.group(2))  # 输出：3

#roup(0) 返回整个匹配的内容
#group(1)、group(2) 分别返回第一个、第二个分组的内容

####常用修饰符####
#re.IGNORECASE 或 re.I：忽略大小写匹配
#re.MULTILINE 或 re.M：多行模式下，^ 和 $ 匹配每一行的开头和结尾
#re.DOTALL 或 re.S：使 . 匹配包括换行在内的所有字符
#re.VERBOSE 或 re.X：允许正则表达式中包含空格和注释，便于阅读

####零宽断言####
#(?=...) 正向前瞻，在当前位置向后检查是否有匹配 ... 的内容
#(?!...) 负向前瞻，检查当前位置向后没有 ...
#(?<=...) 正向后瞻，检查当前位置之前是否有 ...
#(?<!...) 负向后瞻，检查当前位置之前没有 ...

# 匹配"hello"后面跟数字的情况
import re
result = re.search(r'hello(?=\d)', 'hello2 world')
print(result)  # 输出 <re.Match object; span=(0, 5), match='hello'>

result = re.search(r'(?<=hello)\d', 'hello2 world')
print(result)  # 输出 <re.Match object; span=(5, 6), match='2'>

####Match 对象的常用方法####
#.group()：返回匹配的字符串
#.start()：返回匹配开始的位置
#.end()：返回匹配结束的位置
#.span()：返回匹配的 (start, end) 元组
import re
match = re.search(r'\d+', 'I have 2 apples and 3 oranges')
if match:
    print(match.group())  # 输出 '2'
    print(match.start())  # 输出 7
    print(match.end())    # 输出 8
    print(match.span())   # 输出 (7, 8)

################################################################
#1.匹配字符串"手机号码188653752731"中的 188653752731
import re
pattern = re.compile(r'188\d{8}')
str = '手机号码188653752731'
result = pattern.search(str)
print(result.group())
"""
################################################################
#生成一个nginx的访问日志文件，并用python分析统计访问量、状态码分布、访问 IP 地址、URL 的访问频率

#生成日志
import random
import time
from datetime import datetime, timedelta

def generate_log():
    ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    urls = ["/index.html", "/about.html", "/contact.html"]
    statuses = [200, 404, 500]
    referers = ["http://example.com", "http://google.com", "-"]
    user_agents = [
        "Mozilla/5.0",
        "Chrome/90.0",
        "Safari/537.36"
    ]

    with open("access.log", "w") as f:
        for _ in range(100):  # 生成100行日志
            ip = random.choice(ips)
            url = random.choice(urls)
            status = random.choice(statuses)
            referer = random.choice(referers)
            user_agent = random.choice(user_agents)
            byte_size = random.randint(100, 5000)
            timestamp = datetime.now() - timedelta(minutes=random.randint(0, 60))
            log_line = f'{ip} - - [{timestamp.strftime("%d/%b/%Y:%H:%M:%S +0000")}] "GET {url} HTTP/1.1" {status} {byte_size} "{referer}" "{user_agent}"\n'
            f.write(log_line)

generate_log()


#Python 代码来读取日志文件，并进行分析，比如统计访问量、状态码分布、访问 IP 地址、URL 的访问频率等
import re
from collections import Counter

# 定义正则表达式模式
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<time>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) (?P<protocol>\S+)" (?P<status>\d+) (?P<size>\d+) "(?P<referer>[^"]+)" "(?P<user_agent>[^"]+)"'
)

# 读取日志文件并解析
with open("access.log") as f:
    logs = [log_pattern.match(line).groupdict() for line in f if log_pattern.match(line)]

# 统计访问次数
total_requests = len(logs)
print(f"总请求数：{total_requests}")

# 统计状态码分布
status_counter = Counter(log['status'] for log in logs)
print("状态码分布：", status_counter)

# 统计每个 IP 的访问次数
ip_counter = Counter(log['ip'] for log in logs)
print("访问次数最多的 IP：", ip_counter.most_common(5))

# 统计 URL 的访问次数
url_counter = Counter(log['url'] for log in logs)
print("访问次数最多的 URL：", url_counter.most_common(5))

################################################################
#queue 模块提供了用于多线程编程的多种线程安全的队列。
#queue 模块中的队列在多线程程序中常用于线程间的数据传递与任务调度

#队列类型
#FIFO 队列 (Queue)：先进先出队列，最常用的队列类型。
#LIFO 队列 (LifoQueue)：后进先出队列（类似堆栈）。
#优先级队列 (PriorityQueue)：可以按照优先级顺序出队，优先级数值越小优先级越高

#FIFO 队列（Queue）

import queue
q = queue.Queue(maxsize=10)  # maxsize 为队列最大长度，0 或负数表示不限制

# LIFO 队列（LifoQueue
lq = queue.LifoQueue(maxsize=10)

#优先级队列（PriorityQueue）
pq = queue.PriorityQueue(maxsize=10)


####常用方法####
#put(item, block=True, timeout=None)
#将 item 插入到队列尾部。默认是阻塞模式，若队列已满则会等待直到队列有空位
#block：是否阻塞，默认 True。
#timeout：等待的超时时间（秒），仅在 block=True 时生效

q.put("data")  # 将 "data" 加入队列
q.put("data", block=False)  # 如果队列满了立即报错

#get(block=True, timeout=None)
#从队列头部移除并返回一个元素。默认是阻塞模式，若队列为空则会等待直到队列不为空
#block：是否阻塞，默认 True。
#timeout：等待的超时时间（秒），仅在 block=True 时生效。

data = q.get()  # 获取并移除队列头部元素
data = q.get(block=False)  # 如果队列为空立即报错

#task_done()
#告知队列当前任务已完成。一般在调用 get() 后立即调用 task_done()。
#此方法用于配合 join() 方法来跟踪未完成的队列任务数
data = q.get()
# 处理 data
q.task_done()  # 标记该任务完成

#join()
#阻塞线程，直到队列中所有的元素都被接收并处理完（即，task_done() 调用数等于 put() 调用数
q.join()  # 等待队列中的所有任务完成

#qsize()
#返回队列的大小（元素数量）。注意：结果可能并不完全准确，因为队列可能正被其他线程操作
print(q.qsize())  # 输出队列中当前的元素数

######多线程中的应用示例######
import threading
import queue
import time
import random

# 创建队列
q = queue.Queue(maxsize=10)

# 生产者线程
def producer(name):
    while True:
        item = random.randint(1, 100)
        q.put(item)
        print(f"{name} 生产了 {item}")
        time.sleep(random.uniform(0.5, 1.5))

# 消费者线程
def consumer(name):
    while True:
        item = q.get()
        print(f"{name} 消费了 {item}")
        q.task_done()
        time.sleep(random.uniform(0.5, 1.5))

# 创建并启动线程
producer_thread = threading.Thread(target=producer, args=("Producer",))
consumer_thread = threading.Thread(target=consumer, args=("Consumer",))
producer_thread.start()
consumer_thread.start()