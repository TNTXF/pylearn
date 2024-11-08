#文件 I/O 操作包括文件的读写、文件的创建和删除等操作
#Python 提供了内置的 open() 函数来处理文件的打开和操作
########################################################################
#file = open("filename.txt", mode)   ###filename.txt 是文件名，mode 是打开文件的模式

#open详细参数：
#open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

#file：字符串，文件路径。可以是相对路径或绝对路径。
#mode：字符串，指定文件的打开模式（详见下文）。
#buffering：整数，控制文件的缓冲方式。默认值为 -1，表示自动选择最佳模式。
    #0：不缓冲，仅用于二进制模式。
    #1：行缓冲，仅用于文本模式。
    #>1：指定缓冲区大小，单位是字节。
#encoding：字符串，指定文件编码类型（如 'utf-8'、'ascii'）。仅适用于文本模式。
#errors：字符串，指定编码错误的处理方式，如 'ignore'、'replace' 等。
#newline：字符串，控制换行符的处理方式。默认为 None（自动处理），可指定为 '\n'、'\r'、'\r\n'。
#closefd：布尔值，指定关闭文件描述符的方式。默认值为 True，表示关闭。
#opener：一个自定义的文件打开函数。需要返回一个有效的文件描述符

########################################################################
# mode主要的模式字符：
    #r：读模式（默认）。文件必须存在，否则会抛出 FileNotFoundError。
    #w：写模式。如果文件已存在，将会覆盖文件内容。如果文件不存在，则创建新文件。
    #a：追加模式。在文件末尾写入数据，不会覆盖现有内容。如果文件不存在，则创建新文件。
    #x：新建模式。如果文件不存在则创建新文件，若文件已存在则抛出 FileExistsError

#文件类型
    #t：文本模式（默认）。以字符串的形式进行读写操作。
    #b：二进制模式。以字节的形式进行读写操作，用于处理二进制文件（如图片、音频文件）

#组合模式
    #r+：读写模式。文件必须存在。可以在文件中任意位置读取和写入数据。
    #w+：读写模式。如果文件已存在，将覆盖文件内容。如果文件不存在，则创建新文件。
    #a+：读写模式。打开文件用于读取和追加写入操作。如果文件不存在，则创建新文件

#二进制模式的组合
    #rb：以二进制方式读取文件。
    #wb：以二进制方式写入文件。如果文件已存在，将覆盖文件内容。
    #ab：以二进制方式打开文件，用于追加写入。
    #rb+：以二进制方式打开文件，进行读写操作。
    #wb+：以二进制方式打开文件，进行读写操作。如果文件已存在，将覆盖文件内容。
    #ab+：以二进制方式打开文件，进行读取和追加写入操作

######################################################################
"""

import os
print(os.getcwd())

# code runner 中勾选 File Directory as cwd 否则是os.getcwd()

#read() 读取全部内容
file = open('example.txt',"r")
content = file.read()
print(content)
file.close()

#readline() 逐行读取
file = open("example.txt", "r")
line = file.readline()

while line:
    print(line,end='')
    line = file.readline()

file.close()

#readlines() 读取所有行并返回列表
file = open("example.txt", "r")
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()


#写入文件, 注意如果文件存在，会被覆盖
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()

#writelines() 写入多行内容，需要传入一个列表，文件存在内容会被覆盖
file = open("example.txt", "w")
file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
file.close()


#文件的追加模式
file = open("example.txt", "a")
file.write("This is an appended line.")
file.close()


#使用 with 语句进行文件操作,使用 with 语句可以自动管理文件的关闭操作,更加安全
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


###文件的其他操作

#tell() 获取当前文件指针位置
with open("example.txt", "r") as file:
    file.read(5)
    print(file.tell())  # 5

#seek(offset[, whence]) 用于移动文件指针到指定位置
#offset：表示移动的字节数
#whence：参考位置（默认为 0），0 表示文件开头，1 表示当前位置，2 表示文件结尾

with open("example.txt", "r") as file:
    file.seek(5, 0)  # 跳转到第6个字节
    print(file.read(5))  # 读取5个字节


#文件的二进制操作,可以用 'b' 模式处理非文本文件（如图像、音频文件等）
with open("image.png",'rb') as file:
    data = file.read()
    print(data)

with open("image_copy.png", "wb") as file:
    data = 'abc'.encode()
    file.write(data)
    file.close()
    #打不开图片了
"""

########################################################################
#实现：有一个文件对其进行单词，不区分大小写



