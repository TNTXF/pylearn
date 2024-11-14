#Python 网络编程是实现网络通信和构建网络应用的重要组成部分，主要通过套接字（Socket）进行数据传输
#Python 提供了多个库来支持网络编程，其中最常用的是标准库中的 socket 模块以及一些第三方库（如 requests、asyncio 等）

####1. 基础概念#####
#网络通信通常涉及客户端和服务器，客户端向服务器发起请求，服务器接收请求并返回响应
    #套接字（Socket）：用于建立网络连接和数据传输的通信端点。每个套接字由地址（IP 地址）和端口号组成。
    #协议：通信协议决定了数据在网络中的传输方式，最常用的是 TCP（传输控制协议）和 UDP（用户数据报协议）。
    #客户端和服务器：客户端发起请求，服务器监听并响应客户端请求

####socket 模块####
#常用方法
""" 
socket()：创建套接字对象。
bind()：绑定地址(IP地址和端口)。
listen()：监听连接（仅在服务器端使用）。
accept()：接收连接请求，返回一个新的套接字和客户端地址。#默认阻塞
connect()：连接到远程主机（客户端使用）。
send() / sendall()：发送数据。
recv()：接收数据。
close()：关闭连接
"""



#---------------TCP Server 示例代码---------------#
""" 
import socket
import logging
logging.basicConfig(level=logging.INFO,format='%(thread)s %(threadName)s %(message)s')

# 创建 TCP/IP 套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定到端口
server_socket.bind(('localhost', 65432))
server_socket.listen()

logging.info("waitting for connect...")

while True:
    # 等待连接
    client_socket, addr = server_socket.accept()
    logging.info(f"connect from --> {addr}")
    logging.info(f"client socket: {client_socket}")

    # 接收数据
    data = client_socket.recv(1024)
    if data:
        logging.info(f"data messages: {data.decode()}")
        client_socket.sendall(b"data received")

    # 关闭连接
    client_socket.close() """


#-------------------------TCP Client 示例代码----------------------#
""" 
import socket
import logging

logging.basicConfig(level=logging.INFO,format='%(thread)s %(threadName)s %(message)s')

# 创建 TCP/IP 套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
client_socket.connect(('localhost', 65432))

# 发送数据
client_socket.sendall(b"hello server")

# 接收响应
data = client_socket.recv(1024)
logging.info(f"接收自服务器: {data.decode()}") 

# 关闭连接
client_socket.close()"""

#-----------------------UDP Server示例-----------------------#
#UDP 协议不需要连接，数据通过 sendto() 和 recvfrom() 发送和接收
""" 
import socket
import logging
logging.basicConfig(level=logging.INFO,format='%(thread)s %(threadName)s %(message)s')

# 创建 UDP/IP 套接字
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定到端口
udp_server_socket.bind(('localhost', 65432))

logging.info("UDP Server is waitting for data...")

while True:
    data, addr = udp_server_socket.recvfrom(1024)
    print(f"received data from --> {addr} : {data.decode()}")
    udp_server_socket.sendto(b"data received", addr)
 """
#-----------------------UDP Client示例-----------------------#
""" 
import socket
import logging
logging.basicConfig(level=logging.INFO,format='%(thread)s %(threadName)s %(message)s')

# 创建 UDP/IP 套接字
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据
udp_client_socket.sendto(b"Hello,UDP Server", ('localhost', 4023))

# 接收响应
data, server = udp_client_socket.recvfrom(1024)
logging.info(data.decode())

# 关闭套接字
udp_client_socket.close() """


####3. 高级功能#####
#asyncio（异步网络编程）
#Python 的 asyncio 库允许进行异步 I/O 操作，特别适用于高并发的网络应用（如 HTTP 服务器、WebSocket 等）
""" 
import asyncio

async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Received {message} from {addr}")
    writer.write(data)
    await writer.drain()
    print("Closing the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()

asyncio.run(main()) """


#requests 是 Python 中非常流行的第三方库，简化了 HTTP 请求的发送和响应的处理。它使得网络请求更加简单和人性化
""" 
import requests

# 发送 GET 请求
response = requests.get('https://httpbin.org/get')
print(response.text)

# 发送 POST 请求
data = {'name': 'Alice', 'age': 25}
response = requests.post('https://httpbin.org/post', data=data)
print(response.text) """

########################################################################
########################################################################
#写一个群聊程序

# 服务器端
""" 
import socket
import threading

# 存储所有连接的客户端套接字
clients = []

# 广播消息给所有客户端
def broadcast(message, client_socket):
    for client in clients:
        # 不给自己发送消息
        if client != client_socket:
            try:
                client.send(message)
            except:
                # 如果发送失败，删除该客户端
                clients.remove(client)

# 处理每个客户端的消息
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)  # 接收消息
            if message:
                print(f"接收到消息: {message.decode()}")
                broadcast(message, client_socket)  # 广播消息
            else:
                break
        except:
            break

    # 客户端断开连接，移除该客户端
    clients.remove(client_socket)
    client_socket.close()

# 服务器主函数
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 65432))
    server_socket.listen(5)
    print("服务器启动，等待客户端连接...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"客户端 {addr} 已连接")
        clients.append(client_socket)
        
        # 启动一个新线程处理客户端
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server() 
 """

#客户端代码
""" 
import socket
import threading

# 接收消息的函数
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"\n{message.decode()}")
            else:
                break
        except:
            break

# 发送消息的函数
def send_messages(client_socket):
    while True:
        message = input()  # 用户输入消息
        if message:
            client_socket.send(message.encode())

# 客户端主函数
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('38.57.12.49', 65432))

    print("已连接到服务器，开始聊天...")

    # 启动线程接收消息
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # 启动线程发送消息
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    start_client() """


################################################################
################################################################
#Python的socketserver模块是一个高级的网络服务框架，用于处理网络请求。它基于socket模块
#socketserver模块包含以下几个主要组件

####主要组件####

    #BaseServer：所有服务器类型的基类。它定义了基本的服务器行为，如接收连接请求、绑定端口等。
    #TCPServer：继承自BaseServer，用于处理基于TCP协议的网络请求。
    #UDPServer：继承自BaseServer，用于处理基于UDP协议的网络请求。
    #StreamRequestHandler：用于处理基于流的请求（例如TCP连接）。每个请求都会创建一个StreamRequestHandler对象来处理。
    #DatagramRequestHandler：用于处理基于数据报的请求（例如UDP连接）。每个请求都会创建一个DatagramRequestHandler对象来处理。

####socketserver 模块的使用####

#创建一个简单的 TCP 服务器
""" 
import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # 处理客户端请求
        data = self.request.recv(1024).strip()  # 接收数据
        print(f"Received data: {data}")
        self.request.sendall(data)  # 回送数据

if __name__ == "__main__":
    # 创建一个TCP服务器，监听localhost:9999
    server = socketserver.TCPServer(('localhost', 9999), MyHandler)
    print("Server running...")
    server.serve_forever() """


# 使用socketserver创建一个UDP服务器
""" 
import socketserver

class MyUDPHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        data = self.request[0].strip()  # 获取接收到的数据
        socket = self.request[1]  # 获取客户端的socket
        print(f"Received UDP data: {data}")
        socket.sendto(data, self.client_address)  # 回送数据

if __name__ == "__main__":
    # 创建一个UDP服务器，监听localhost:9999
    server = socketserver.UDPServer(('localhost', 9999), MyUDPHandler)
    print("Server running...")
    server.serve_forever() """

####多线程支持####
#socketserver模块默认是单线程的，也就是说每个请求会按顺序依次处理。
#要支持并发处理请求，可以使用ThreadingMixIn类来创建多线程服务器

""" 
import socketserver

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        print(f"Received data: {data}")
        self.request.sendall(data)

if __name__ == "__main__":
    server = ThreadedTCPServer(('localhost', 9999), MyHandler)
    print("Server running...")
    server.serve_forever() """


####高级功能####
#请求超时：可以设置服务器的超时机制。如果请求在指定时间内没有处理完，可以让服务器自动中止该请求。
#多种请求处理方式：socketserver支持多种不同的请求处理方式，比如同步、线程池、进程池等。

#信号处理：服务器运行过程中可能需要处理终止信号，例如Ctrl+C。
#可以通过捕捉KeyboardInterrupt异常或使用signal模块来优雅地关闭服务器



################################################################
################################################################
#Python中的IO多路复用是一种高效的I/O操作方式，通常用于处理多个I/O事件，如网络连接、文件读写等
#Python中有几个模块可以实现IO多路复用的功能，主要包括select、poll、和epoll模块。
#这些模块允许程序在一个线程内同时处理多个I/O操作，适合在高并发情况下提升性能

####select模块####
#select模块提供了基础的IO多路复用功能，主要有select.select方法。
#在Linux和Windows上都支持，但在高并发情况下性能较差，原因是它对监控的文件描述符有数量限制

#select.select接收三个列表：读、写、异常，并在指定超时时间内监控这些文件描述符的状态
""" 
import select
import socket

# 创建一个非阻塞的socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)
server_socket.setblocking(False)


# 监控输入列表
inputs = [server_socket]
outputs = []

while inputs:
    # select方法返回三个列表
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    for s in readable:
        if s is server_socket:
            # 处理新连接
            conn, addr = s.accept()
            print('Connected by', addr)
            conn.setblocking(False)
            inputs.append(conn)
        else:
            # 处理已有连接
            data = s.recv(1024)
            if data:
                # 处理数据
                outputs.append(s)
            else:
                inputs.remove(s)
                s.close()

    for s in writable:
        # 向客户端写数据
        s.send(b"Response")
        outputs.remove(s)

    for s in exceptional:
        # 处理异常情况
        inputs.remove(s)
        s.close() """


####poll模块####
#poll是select的改进版，克服了文件描述符限制的问题。在Linux上有更好的性能，但在Windows上不支持

#poll方法提供的接口与select不同。你需要注册文件描述符并设置它们的事件掩码
""" 
import select
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)
server_socket.setblocking(False)

# 使用poll来监控事件
poller = select.poll()
poller.register(server_socket, select.POLLIN)

fd_to_socket = {server_socket.fileno(): server_socket}

while True:
    events = poller.poll()
    for fd, flag in events:
        sock = fd_to_socket[fd]
        
        if flag & select.POLLIN:
            if sock is server_socket:
                # 接受新连接
                conn, addr = sock.accept()
                print('Connected by', addr)
                conn.setblocking(False)
                fd_to_socket[conn.fileno()] = conn
                poller.register(conn, select.POLLIN)
            else:
                # 读取数据
                data = sock.recv(1024)
                if data:
                    poller.modify(sock, select.POLLOUT)
                else:
                    poller.unregister(sock)
                    sock.close()
                    del fd_to_socket[fd]

        elif flag & select.POLLOUT:
            # 发送数据
            sock.send(b"Response")
            poller.modify(sock, select.POLLIN)
        
        elif flag & select.POLLERR:
            # 处理错误
            poller.unregister(sock)
            sock.close()
            del fd_to_socket[fd] """


####epoll模块####
#epoll是Linux特有的IO多路复用实现。相比select和poll，epoll更适合处理大量连接，适用于高并发的服务器
""" 
import select
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)
server_socket.setblocking(False)

epoll = select.epoll()
epoll.register(server_socket.fileno(), select.EPOLLIN)

fd_to_socket = {server_socket.fileno(): server_socket}

while True:
    events = epoll.poll()
    for fd, event in events:
        sock = fd_to_socket[fd]
        
        if event & select.EPOLLIN:
            if sock is server_socket:
                # 接受新连接
                conn, addr = sock.accept()
                print('Connected by', addr)
                conn.setblocking(False)
                fd_to_socket[conn.fileno()] = conn
                epoll.register(conn.fileno(), select.EPOLLIN)
            else:
                # 读取数据
                data = sock.recv(1024)
                if data:
                    epoll.modify(fd, select.EPOLLOUT)
                else:
                    epoll.unregister(fd)
                    sock.close()
                    del fd_to_socket[fd]
        
        elif event & select.EPOLLOUT:
            # 发送数据
            sock.send(b"Response")
            epoll.modify(fd, select.EPOLLIN)
        
        elif event & select.EPOLLHUP:
            # 处理挂起
            epoll.unregister(fd)
            sock.close()
            del fd_to_socket[fd] """
