#Python 网络编程是实现网络通信和构建网络应用的重要组成部分，主要通过套接字（Socket）进行数据传输
#Python 提供了多个库来支持网络编程，其中最常用的是标准库中的 socket 模块以及一些第三方库（如 requests、asyncio 等）

####1. 基础概念#####
#网络通信通常涉及客户端和服务器，客户端向服务器发起请求，服务器接收请求并返回响应
    #套接字（Socket）：用于建立网络连接和数据传输的通信端点。每个套接字由地址（IP 地址）和端口号组成。
    #协议：通信协议决定了数据在网络中的传输方式，最常用的是 TCP（传输控制协议）和 UDP（用户数据报协议）。
    #客户端和服务器：客户端发起请求，服务器监听并响应客户端请求

####socket 模块####

#---------------TCP Server 示例代码---------------#
""" 
import socket

# 创建一个 TCP 套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
server_socket.bind(('localhost', 12345))

# 开始监听客户端请求
server_socket.listen(5)
print("Server listening on port 12345")

# 等待客户端连接
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# 接收数据
data = client_socket.recv(1024)
print(f"Received data: {data.decode()}")

# 发送响应
client_socket.send("Hello, Client!".encode())

# 关闭连接
client_socket.close()
server_socket.close() 
"""


#-------------------------TCP Client 示例代码----------------------#
""" 
import socket

# 创建一个 TCP 套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
client_socket.connect(('localhost', 12345))

# 发送数据
client_socket.send("Hello, Server!".encode())

# 接收服务器响应
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

# 关闭连接
client_socket.close() 
"""

#-----------------------UDP Server示例-----------------------#
""" 
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Received data: {data.decode()} from {addr}")
    server_socket.sendto("Hello, UDP Client!".encode(), addr) 
"""
#-----------------------UDP Client示例-----------------------#
""" 
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据
client_socket.sendto("Hello, Server!".encode(), ('localhost', 12345))

# 接收数据
data, server = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode()}")

client_socket.close() 
"""

####3. 高级功能#####
#asyncio（异步网络编程）
#Python 的 asyncio 库允许进行异步 I/O 操作，特别适用于高并发的网络应用（如 HTTP 服务器、WebSocket 等）
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

asyncio.run(main())


#requests 是 Python 中非常流行的第三方库，简化了 HTTP 请求的发送和响应的处理。它使得网络请求更加简单和人性化
import requests

# 发送 GET 请求
response = requests.get('https://httpbin.org/get')
print(response.text)

# 发送 POST 请求
data = {'name': 'Alice', 'age': 25}
response = requests.post('https://httpbin.org/post', data=data)
print(response.text)

