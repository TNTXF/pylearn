#python 中的线程是一种轻量级的并发机制，允许程序同时运行多个执行流（线程），以实现多任务处理

#线程与进程
#线程：线程是进程中的一个执行流，可以共享进程的内存空间和资源。一个进程可以包含多个线程。
#进程：进程是资源分配的最小单位，线程是 CPU 调度的最小单位。

####全局解释器锁（GIL）####
#Python 中的 GIL（Global Interpreter Lock）限制了在同一时间只有一个线程可以执行 Python 字节码，
#因此 Python 的多线程在 CPU 密集型任务上效果有限
#对于 I/O 密集型任务（如文件读写、网络请求），多线程依然有显著的优势


####threading 模块：提供了创建和管理线程的类和方法####
"""
#threading.Thread：参数
import threading
import time

def greet(name, delay, greeting="Hello"):
    time.sleep(delay)
    print(f"{greeting}, {name}!")

# 创建带有所有参数的线程
thread = threading.Thread(
    target=greet,         # 设置线程的目标函数
    args=("Alice", 2),    # 位置参数
    kwargs={"greeting": "Hi"},  # 关键字参数
    name="GreetingThread",      # 线程名称
    daemon=True                # 守护线程标志
)

thread.start()
print("Main thread continues.")
thread.join()
print("Main thread finished.")
"""
##################################################################
"""
#方法 1：使用 threading.Thread 创建线程

import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

# 创建线程
thread = threading.Thread(target=print_numbers)

# 启动线程
thread.start()
# 等待线程结束
thread.join()
print("Thread finished")

#方法 2：继承 Thread 类创建自定义线程类
#继承 threading.Thread，并重写 run 方法来定义线程执行的任务

import threading
import time

class NumberThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(f"Number: {i}")
            time.sleep(1)

# 创建并启动线程
thread = NumberThread()
thread.start()
thread.join()
print("Thread finished")

#常用的线程属性和方法
    #start()：启动线程，调用线程的 run 方法; start() 只能调用一次，如果多次调用会抛出 RuntimeError

    #run()：线程的入口函数，定义线程要执行的任务
    #run() 方法会在调用 start() 后自动执行。可以重写 run() 方法来定义线程的具体任务

    #join(timeout=None)：等待线程结束，如果设置 timeout 参数，则等待指定时间。
    #在主线程中调用 run() 方法等待子线程结束后再继续执行后续代码

    #is_alive()：检查线程是否正在运行

###thearding的其他方法：
    #current_thread()：返回当前线程对象

    #main_thread()：返回主线程对象

    #active_count()：返回正在运行的线程数量

    #enumerate()：返回一个包含所有线程对象的列表

    #get_ident()：返回线程的 ID




####线程同步####
#线程在访问共享资源时可能会出现竞争条件（race condition），导致数据不一致。为了避免此问题，
#可以使用同步机制，例如锁（Lock）和条件变量（Condition）

#Lock 是一种线程同步原语，用于确保同一时间只有一个线程可以访问共享资源
import threading

balance = 0
balance_lock = threading.Lock()

def deposit(amount):
    global balance
    with balance_lock:  # 使用 with 语句自动加锁和解锁
        temp = balance
        temp += amount
        balance = temp

threads = [threading.Thread(target=deposit, args=(100,)) for _ in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f"Final balance: {balance}")

#条件变量用于复杂的线程同步场景，通常结合 Lock 使用，让线程等待特定的条件满足后继续执行
import threading

condition = threading.Condition()
data_ready = False

def producer():
    global data_ready
    with condition:
        print("Producing data...")
        data_ready = True
        condition.notify()  # 通知消费者线程数据已准备好

def consumer():
    with condition:
        condition.wait()  # 等待通知
        print("Consuming data...")

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

consumer_thread.start()
producer_thread.start()

consumer_thread.join()
producer_thread.join()


####线程通信####
#线程之间可以使用 Queue 来安全地传递数据

import threading
import queue

q = queue.Queue()

def producer():
    for i in range(5):
        q.put(i)
        print(f"Produced {i}")

def consumer():
    while True:
        item = q.get()
        if item is None:  # 结束标志
            break
        print(f"Consumed {item}")
        q.task_done()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # 放入结束标志
consumer_thread.join()

####守护线程（Daemon Thread）####
#守护线程在主线程结束时自动终止。在创建线程时，可以通过设置 daemon 属性来指定线程为守护线程
import threading
import time

def background_task():
    while True:
        print("Running background task...")
        time.sleep(1)

thread = threading.Thread(target=background_task)
thread.daemon = True  # 将线程设置为守护线程
#可以认为daemon线程没有non-daemon线程重要，daemon 线程会在主线程结束后结束
thread.start()

time.sleep(3)
print("Main program finished")  # 主程序结束后守护线程也随之终止


####线程池####
#使用线程池可以更高效地管理大量线程
from concurrent.futures import ThreadPoolExecutor

def task(n):
    print(f"Processing {n}")
    return n * 2

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(5))

print(list(results))


####线程的常见问题###
#线程安全：多个线程同时访问共享数据时，可能导致数据错误。使用锁、条件变量等同步机制可以解决这一问题。
#死锁：多个线程相互等待对方释放资源，导致程序陷入死锁。尽量减少锁的使用，或避免多锁嵌套。
#GIL 限制：GIL 会限制 Python 多线程的并行性，在 CPU 密集型任务中不一定提高效率。
#对于 CPU 密集型任务，可以考虑使用多进程 multiprocessing

####线程与 GIL 的优化建议####
#多进程（multiprocessing）：适用于 CPU 密集型任务，绕过 GIL。
#异步编程（asyncio）：适用于 I/O 密集型任务，可以在单线程中高效处理并发任务

"""
###################################################################
#logging模块
#logging 模块有五个日志级别，从低到高分别是
    #DEBUG（10）：用于调试，非常详细的信息，适合诊断问题。
    #INFO（20）：确认程序按预期工作的信息。
    #WARNING（30）：提示某些情况可能会导致问题或错误，程序仍然运行。
    #ERROR（40）：记录更严重的问题，程序有错误但未崩溃。
    #CRITICAL（50）：记录非常严重的问题，程序可能无法继续运行
"""
#基本用法
import logging

logging.basicConfig(level=logging.INFO)  # 设置日志级别
logging.debug("This is a debug message") #低于设置的级别不显示消息
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#logging 模块的组件
    #Logger：记录日志的接口，是最常用的入口。可以通过 logging.getLogger() 获取。
    #Handler：处理日志记录的方式，如输出到控制台、文件或网络。
    #Formatter：格式化日志输出样式，可以自定义日志消息的格式。
    #Filter：用于细化日志输出，可以控制特定日志的输出。

#自定义日志格式
    #%(levelname)s：日志级别名称。
    #%(asctime)s：日志的时间戳。
    #%(message)s：日志消息内容。
    #%(name)s：Logger 的名称。
    #%(filename)s：调用日志的文件名

import logging

# 设置日志格式
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.debug("This is a debug message")
logging.info("This is an info message")


#将日志写入文件
import logging
logging.basicConfig(
    filename='app.log',            # 输出到 app.log 文件
    filemode='a',                   # 追加模式，默认为 'a'
    level=logging.WARNING,          # 设置日志级别为 WARNING
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.warning("This is a warning message")  # 会记录在 app.log 文件中
logging.error("This is an error message")     # 也会记录在文件中

#通过 Logger、Handler 和 Formatter 自定义日志
import logging

# 创建 Logger 对象
logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)  # 设置日志级别

# 创建控制台 Handler 并设置级别
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建文件 Handler 并设置级别
file_handler = logging.FileHandler("my_app.log")
file_handler.setLevel(logging.ERROR)

# 创建 Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 将 Formatter 添加到 Handler
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将 Handler 添加到 Logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 日志输出
logger.debug("This is a debug message")   # 仅输出到控制台
logger.info("This is an info message")    # 输出到控制台
logger.warning("This is a warning message")  # 输出到控制台
logger.error("This is an error message")  # 输出到控制台和文件
logger.critical("This is a critical message")  # 输出到控制台和文件
"""
###################################################################
"""
import threading
import time
a = threading.local()
def worker():
    a.x = 0
    for i in range(100):
        #time.sleep(0.01)
        a.x += 1
    print(threading.current_thread(),a.x)
    
for i in range(10):
    t = threading.Thread(target=worker)
    t.start()
"""

################################################################


import threading
import time
a = threading.local()
def worker():
    a.x = 0
    for i in range(100):
        #time.sleep(0.01)
        a.x += 1
    print(threading.current_thread(),a.x)
    
for i in range(10):
    t = threading.Thread(target=worker)
    t.start()
