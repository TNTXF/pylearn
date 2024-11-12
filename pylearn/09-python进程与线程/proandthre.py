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

########################################
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
################################################################
#Python 提供了 multiprocessing 模块，便于创建和管理多个进程
"""
#基本的多进程创建：Process 类
#Process 类是 multiprocessing 模块的核心类，用于创建和启动新进程
from multiprocessing import Process

def worker():
    print("Worker process is running")

if __name__ == "__main__":
    p = Process(target=worker)  # 创建进程对象
    p.start()  # 启动进程
    p.join()   # 等待进程完成
#定义了一个 worker 函数，并使用 Process 创建一个进程对象 p
#start() 方法启动进程，join() 方法让主进程等待子进程完成

#####进程间通信####
#Python 提供了多种进程间通信的方式，如队列（Queue）、管道（Pipe）和共享内存对象
#队列（Queue）：用于在进程之间安全地传递数据，类似于线程的 queue.Queue
from multiprocessing import Process, Queue

def producer(q):
    q.put("Hello from producer")

def consumer(q):
    print(q.get())

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


#管道（Pipe）：实现双向数据传输，适合双进程通信
from multiprocessing import Process, Pipe

def worker(conn):
    conn.send("Hello from worker")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=worker, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # 接收子进程发送的消息
    p.join()


#共享内存（Value 和 Array）：在多个进程间共享数据
from multiprocessing import Process, Value, Array

def increment(shared_val):
    shared_val.value += 1

if __name__ == "__main__":
    val = Value("i", 0)  # 创建整数共享变量
    p = Process(target=increment, args=(val,))
    p.start()
    p.join()
    print(val.value)  # 输出 1

#进程池（Pool）
#Pool 提供了批量创建进程的方法，可以限制最大并发进程数量，适合并行执行大量任务
from multiprocessing import Pool

def worker(x):
    return x * x

if __name__ == "__main__":
    with Pool(4) as pool:  # 创建 4 个并发进程
        results = pool.map(worker, [1, 2, 3, 4])  # 并行执行任务
        print(results)  # 输出 [1, 4, 9, 16]

#Pool 中常用的方法包括：
    #map()：类似于内置的 map() 函数，接受可迭代对象并将任务分配给各个进程。
    #apply()：单次任务分配给一个进程，返回结果。
    #apply_async()：异步任务分配，适合需要在执行过程中处理结果的场景

#### 异常处理和退出####
#在多进程中，子进程遇到的异常不会传递到主进程，因此需要单独捕获并处理
"""

####为什么多进程创建和启动要放在if __name__ == "__main__":里
#1. 避免递归进程创建
""" 当 Python 脚本运行时，每个新创建的子进程都会重新加载该脚本。
没有 if __name__ == "__main__": 的保护，子进程会重复执行整个脚本的代码，而不是仅执行目标函数。
这会导致每个子进程不断创建新的子进程，最终陷入无限递归，耗尽系统资源 """

#2. 平台兼容性
""" 在 Unix 系统（如 Linux）上，fork() 系统调用用于创建进程，子进程会自动继承父进程的代码和内存空间
因此通常不会遇到无限递归问题。
然而，在 Windows 和 macOS 上，Python 使用了 spawn 方法来创建进程，它会重新导入主模块，
因此没有 if __name__ == "__main__": 的保护会导致重复导入并运行脚本中的内容 """

#在Linux上测试
""" 
////////////////////////////////
root@HK-BGP:~  $ python test.py 
1
root@HK-BGP:~  $ cat test.py 
from multiprocessing import Process, Value, Array

def increment(shared_val):
    shared_val.value += 1

val = Value("i", 0)  # 创建整数共享变量
p = Process(target=increment, args=(val,))
p.start()
p.join()
print(val.value)  # 输出 1 
//////////////////////////////
"""

#__name__ 变量的作用
""" Python 运行脚本时，__name__ 变量的值会根据脚本是直接运行还是被导入而有所不同：

    如果脚本是直接运行的，__name__ 的值为 "__main__"。
    如果脚本被作为模块导入，__name__ 的值为模块名。
通过 if __name__ == "__main__": 结构，只有在脚本被直接运行时才会执行进程创建的代码，
而在模块导入或子进程重新加载时不会执行 """