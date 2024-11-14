#asyncio模块是Python用于实现异步编程的标准库
#它支持单线程并发运行多个任务，通常用于I/O密集型操作，例如网络请求、文件读写等。在异步编程中

####基本概念####
    #协程（Coroutine）：协程是能够暂停和恢复的函数，通过async def定义。协程只有在被await时才会执行。
    #事件循环（Event Loop）：asyncio的核心，用于调度并执行协程任务。通过事件循环，将异步任务的执行交替进行，从而实现单线程的并发处理。
    #任务（Task）：任务是协程在事件循环中运行的对象，可以通过asyncio.create_task来生成任务。
    #Future：代表一个异步操作的最终结果，通常由任务对象创建和使用
    #可以通过async def语法定义协程。协程函数返回一个coroutine对象，必须在事件循环中执行（如通过await或asyncio.run等）

####协程的状态####
    #未开始：协程定义完成但未开始运行。
    #暂停：协程遇到await语句，控制权交回事件循环。
    #完成：协程执行完毕，返回结果或抛出异常。

####基本用法####
""" 
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # 异步等待 1 秒
    print("World")
#在Python 3.7及以上版本，使用asyncio.run函数启动事件循环并执行协程
asyncio.run(say_hello()) """


####并发运行任务####
#asyncio允许同时执行多个任务，通常通过asyncio.create_task函数将协程包装成任务
""" 
import asyncio

async def task1():
    print("Start task 1")
    await asyncio.sleep(2)
    print("End task 1")

async def task2():
    print("Start task 2")
    await asyncio.sleep(1)
    print("End task 2")

async def main():
    task_a = asyncio.create_task(task1())
    task_b = asyncio.create_task(task2())
    await task_a  # 等待task_a完成
    await task_b  # 等待task_b完成

asyncio.run(main()) """


#### 等待多个任务####
#要并发运行多个任务并等待它们全部完成，可以使用asyncio.gather。
""" 
import asyncio

async def download_data(i):
    print(f"Start downloading {i}")
    await asyncio.sleep(1)
    print(f"Finished downloading {i}")
    return f"Data {i}"

async def main():
    # 同时运行多个下载任务并等待所有任务完成
    results = await asyncio.gather(
        download_data(1),
        download_data(2),
        download_data(3)
    )
    print("All downloads complete:", results)

asyncio.run(main()) """


####超时控制####
#asyncio.wait_for允许为异步操作设置超时时间
""" 
import asyncio

async def fetch_data():
    await asyncio.sleep(5)
    return "Data fetched"

async def main():
    try:
        data = await asyncio.wait_for(fetch_data(), timeout=2)
        print(data)
    except asyncio.TimeoutError:
        print("Fetching data timed out!")

asyncio.run(main()) """


####取消任务####
#在某些情况下，任务可能需要被取消。例如，一个任务超时或由于其他条件不再需要执行时，可以调用task.cancel()
""" 
import asyncio

async def long_task():
    try:
        print("Starting long task...")
        await asyncio.sleep(5)
        print("Long task completed")
    except asyncio.CancelledError:
        print("Long task was cancelled!")

async def main():
    task = asyncio.create_task(long_task())
    await asyncio.sleep(1)
    task.cancel()  # 取消任务
    await task  # 等待任务取消完成

asyncio.run(main()) """


####阻塞任务与异步任务的混用####
#在asyncio中，可以通过run_in_executor将阻塞函数放到线程池或进程池中执行，以避免阻塞事件循环
""" 
import asyncio
import time

def blocking_task():
    print("Blocking task starting...")
    time.sleep(3)  # 阻塞操作
    print("Blocking task completed")

async def main():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, blocking_task)  # 在线程池中运行阻塞任务

asyncio.run(main()) """


####asyncio高级功能####
#asyncio.Queue是一个异步队列，通常用于在协程之间传递数据
""" 
import asyncio

async def producer(queue):
    for i in range(5):
        await queue.put(i)
        print(f"Produced {i}")
        await asyncio.sleep(1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main()) """


#在协程中处理共享资源时，可以使用asyncio.Lock防止数据竞争
""" 
import asyncio

async def task(lock):
    async with lock:  # 使用锁保证同步访问
        print("Task acquired lock")
        await asyncio.sleep(1)
    print("Task released lock")

async def main():
    lock = asyncio.Lock()
    await asyncio.gather(task(lock), task(lock))

asyncio.run(main()) """


#################################################################
#################################################################
#aiohttp是Python中一个高效的异步HTTP客户端和服务器框架，基于asyncio库构建
#适用于高并发的HTTP请求处理场景。它主要分为客户端和服务器两部分

#pip install aiohttp

####aiohttp客户端详解####
#aiohttp客户端适用于发起HTTP请求，常用于爬虫、API调用等。
#使用aiohttp客户端时，Session对象用于管理和复用连接，提升性能

#在aiohttp中，ClientSession是用来发送HTTP请求的主要对象。使用async with语法确保Session能够自动关闭，避免资源泄漏
#示例：GET请求
""" 
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Status: {response.status}")
            print(f"Content-type: {response.headers['content-type']}")
            text = await response.text()
            print(f"Body: {text[:1000]}")  # 只打印前100个字符

asyncio.run(fetch("https://jsonplaceholder.typicode.com/posts/1")) """

#示例：POST请求
""" 
import aiohttp
import asyncio

async def post_data(url, payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            print(f"Status: {response.status}")
            data = await response.json()
            print(f"Response: {data}")

asyncio.run(post_data("https://jsonplaceholder.typicode.com/posts", {"title": "foo", "body": "bar"})) """

##处理请求参数和响应
""" 
import aiohttp
import asyncio

async def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 1}
    headers = {"User-Agent": "aiohttp-client"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            data = await response.json()
            print(data)

asyncio.run(fetch_data()) """

##异步文件下载
""" 
import aiohttp
import asyncio

async def download_file(url, filepath):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(filepath, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)

url = "https://example.com/largefile.zip"
asyncio.run(download_file(url, "largefile.zip")) """

##异步并发请求
""" 
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://jsonplaceholder.typicode.com/posts/1", 
            "https://jsonplaceholder.typicode.com/posts/2",
            "https://jsonplaceholder.typicode.com/posts/3"]
    results = await asyncio.gather(*[fetch(url) for url in urls])
    for result in results:
        print(result[:100])  # 打印每个响应的前100个字符

asyncio.run(main()) """

## 处理超时与异常
""" 
import aiohttp
import asyncio
from aiohttp import ClientTimeout

async def fetch(url):
    timeout = ClientTimeout(total=2)  # 总超时2秒
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as response:
                return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error: {e}")

asyncio.run(fetch("http://jsonplaceholder.typicode.com/posts/1")) """


####aiohttp服务器详解####

#创建一个基本服务器
""" 
from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, world!")

app = web.Application()
app.router.add_get("/", hello)

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1", port=8080) """

#处理POST请求
""" 
from aiohttp import web

async def handle_post(request):
    data = await request.json()  # 获取JSON数据
    print("Received data:", data)
    return web.json_response({"message": "Data received"})

app = web.Application()
app.router.add_post("/submit", handle_post)

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1", port=8080) """

#设置中间件
""" 
from aiohttp import web

@web.middleware
async def logger_middleware(request, handler):
    print(f"Request path: {request.path}")
    response = await handler(request)
    print(f"Response status: {response.status}")
    return response

async def hello(request):
    return web.Response(text="Hello with middleware!")

app = web.Application(middlewares=[logger_middleware])
app.router.add_get("/", hello)

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1", port=8080) """

#异步WebSocket
""" from aiohttp import web

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            await ws.send_str(f"Hello, {msg.data}")
        elif msg.type == web.WSMsgType.CLOSE:
            break

    return ws

app = web.Application()
app.router.add_get("/ws", websocket_handler)

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1", port=8080) """

#启动和关闭事件
""" 
from aiohttp import web

async def on_startup(app):
    print("Server is starting...")

async def on_cleanup(app):
    print("Server is cleaning up...")

app = web.Application()
app.router.add_get("/", lambda request: web.Response(text="Hello!"))

app.on_startup.append(on_startup)
app.on_cleanup.append(on_cleanup)

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1", port=8080) """

#################################################################
""" Python Web开发中，常用的框架主要有以下几种：
    Flask：轻量级Web框架，设计简洁、易上手，适合小型应用或API。
    Django：全栈框架，功能强大，内置了ORM、认证、模板引擎等组件，适合大型Web应用开发。
    FastAPI：基于asyncio的高性能框架，支持自动生成API文档，适合异步I/O密集型应用。
    Tornado、Sanic：异步Web框架，适合高并发处理，性能优异。 """







