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
"""
#实现：有一个文件对其进行单词，不区分大小写
def count_word_frequency(file_path):
    with open(file_path,"r") as file:
        content = file.read().lower()
        words = content.split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

output = count_word_frequency("example.txt")
sort_output = sorted(output.items(), key=lambda x: x[1], reverse=True)

for word, count in sort_output:
    print(f"{word}: {count}")

"""

#######################################################################
"""
#StringIO 和 BytesIO 是 Python io 模块中的两个类，分别用于在内存中读写字符串和字节数据
#它们的主要作用是提供一种在内存中操作数据的方式，就像操作文件一样，但不需要实际创建文件

#StringIO 用于在内存中读写文本（字符串）数据，主要处理 Unicode 文本

from io import StringIO

# 创建 StringIO 对象
s_io = StringIO()

# 写入数据
s_io.write("Hello, ")
s_io.write("World!")
s_io.seek(0)  # 将文件指针移到开头
print(s_io.read())  # 输出：Hello, World!

#StringIO 的常用场景
    #文本处理：可以在内存中生成文本数据，避免频繁的磁盘 I/O。
    #模拟文件对象：可以将 StringIO 对象传递给需要文件对象的函数，而不必创建实际文件。
    #测试：用于模拟文件输入输出，特别适合单元测试

#---------------

#BytesIO 类似于 StringIO，但它用于处理 二进制数据。
#在需要处理字节流（如图片、音频文件、网络数据等）时特别有用

from io import BytesIO

# 创建 BytesIO 对象
b_io = BytesIO()

# 写入二进制数据
b_io.write(b"Hello, ")
b_io.write(b"World!")
b_io.seek(0)  # 将文件指针移到开头
print(b_io.read())  # 输出：b'Hello, World!'

#BytesIO 的常用场景
    #图像处理：在不创建临时文件的情况下，可以直接在内存中处理图像数据。
    #网络数据：处理字节流，如从网络接收到的二进制数据。
    #文件处理：模拟二进制文件读写操作

#与pandas结合
import pandas as pd
from io import StringIO

data = """name,age
Alice,30
Bob,25
"""
df = pd.read_csv(StringIO(data))
print(df)
"""

######################################################################
"""
#python类文件对象：可以像文件对象一样操作
#io.StringIO 和 io.BytesIO
#网络流对象（如 socket 对象）
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("example.com", 80))
s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
response = s.recv(1024)  # 读取网络响应


#管道（Pipe）
import subprocess

process = subprocess.Popen(["echo", "Hello World"], stdout=subprocess.PIPE)
output = process.stdout.read()
print(output)  # 输出：b'Hello World\n'

#HTTP 响应对象（如 urllib 和 requests 的响应对象
import requests

response = requests.get("https://example.com")
content = response.content  # content 是二进制数据
text = response.text  # text 是字符串


#自定义文件对象
#可以通过实现 __enter__()、__exit__()、read()、write() 等方法来定义自己的 file-like 类
class CustomFile:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def read(self):
        if self.position >= len(self.data):
            return ''
        else:
            result = self.data[self.position:]
            self.position = len(self.data)
            return result

    def write(self, data):
        self.data += data

custom_file = CustomFile("Hello")
print(custom_file.read())
custom_file.write(", World!")
print(custom_file.data)

"""
#####################################################################
"""
#os 模块提供了一些与操作系统交互的便捷方法，涵盖文件和目录操作、系统信息获取、进程管理等功能
# 使得跨平台编程更加方便

####1. 文件和目录操作####

#a. 获取当前工作目录
import os
print(os.getcwd())  # 输出当前工作目录路径

#b. 改变当前工作目录
os.chdir('/path/to/directory')
print(os.getcwd())  # 新的工作目录

#c. 列出目录内容
import os
files = os.listdir('.')
print(files)
       
#d. 创建、删除文件和目录
#os.mkdir(path)：创建一个目录。
#os.makedirs(path)：递归创建目录。
#os.rmdir(path)：删除目录（仅适用于空目录）。
#os.removedirs(path)：递归删除目录。
#os.remove(path)：删除文件   

#e. 重命名和移动文件/目录
os.rename('old_name.txt', 'new_name.txt')


####2. 文件和路径信息####

#a. 获取文件信息=>os.stat(path)：获取文件信息，如大小、权限、最后修改时间等
import os
file_info = os.stat('example.txt')
print(file_info.st_size)  # 文件大小

#b. 路径判断
#os.path.isfile(path)：判断路径是否为文件。
#os.path.isdir(path)：判断路径是否为目录。
#os.path.exists(path)：判断路径是否存在。
#os.path.islink(path)：判断路径是否为符号链接

path = os.path.join('/folder', 'file.txt')
print(path)  # /folder/file.txt

####3. 系统信息####
#a. 获取环境变量
#os.getenv(key, default=None)：获取环境变量。
#os.putenv(key, value)：设置环境变量
import os
home_dir = os.getenv('python_home')

#b. 系统和用户信息
#os.name：获取操作系统名称，常见返回值为 'posix'、'nt' 等。
#os.uname()：获取系统详细信息（仅 Unix 系统）。
#os.getlogin()：获取当前登录的用户名。
#os.getuid() 和 os.getgid()：获取用户和组 ID（仅 Unix 系统）。
#os.getpid()：获取当前进程 ID。
import os
print(os.getlogin())


####4. 进程管理####
os.system('ls')  # 在 Linux 上列出目录内容

output = os.popen('echo Hello World').read()
print(output)

####5. 文件描述符操作####
#os.open(path, flags)：以指定标志打开文件，返回文件描述符。
#os.close(fd)：关闭文件描述符。
#os.read(fd, n)：从文件描述符 fd 中读取 n 字节。
#os.write(fd, string)：将字符串写入文件描述符 fd

#os.chmod(path, mode)：修改文件权限。
#os.chown(path, uid, gid)：修改文件所有者和组（仅 Unix 系统）

####其他常用方法###
#os.urandom(n)：生成 n 个字节的随机数据。
#os.walk(path)：生成目录树的路径、子目录和文件名。适合遍历整个目录树。
"""

################################################################
################################################################
"""
#pathlib 是 Python 3.4 引入的一个模块，用于更加直观、面向对象地操作文件和目录路径
####1. 创建 Path 对象####
from pathlib import Path

# 创建 Path 对象
p = Path("example.txt")
print(p)  # 输出：example.txt

# 创建绝对路径的 Path 对象
p = Path("/home/user/example.txt")

####2. 文件/目录检查与属性####
#a. 路径的检查方法
from pathlib import Path
p = Path("example.txt")
print(p.exists())    # 检查文件是否存在
print(p.is_file())   # 是否为文件
print(p.is_dir())    # 是否为目录

#b. 路径属性
from pathlib import Path
p = Path("D:\\74r1k\pylearn\\5-python文件IO\example.txt")
print(p.name)     # 输出：example.txt
print(p.suffix)   # 输出：.txt
print(p.stem)     # 输出：example
print(p.parent)   # 输出：D:\74r1k\pylearn\5-python文件IO
print(p.parts)    # 输出：('D:\\', '74r1k', 'pylearn', '5-python文件IO', 'example.txt')


####3. 文件和目录操作####
#a. 创建和删除目录
    #mkdir()：创建目录，exist_ok=True 表示若目录已存在不会报错。
    #rmdir()：删除目录（只能删除空目录）
from pathlib import Path
p = Path("test")
p.mkdir(exist_ok=True)  # 创建目录
p.rmdir()               # 删除目录


#b. 创建和删除文件
    #touch()：创建文件（若文件不存在）。
    #unlink()：删除文件

from pathlib import Path
p = Path("example2.txt")
p.touch()    # 创建文件
p.unlink()   # 删除文件

####4. 读写文件####
    #read_text()：读取文件内容（以文本形式）。
    #write_text(data)：写入文本数据。
    #read_bytes()：读取文件内容（以字节形式）。
    #write_bytes(data)：写入字节数据。
from pathlib import Path
p = Path("example.txt")
#p.write_text("Hello, World!")  # 写入文本
print(p.read_text())           # 读取文本

####5. 路径操作####
#a. 拼接路径 :使用 / 运算符拼接路径，使得路径操作更直观
from pathlib import Path
p = Path("/home") / "user" / "example.txt"
print(p)  # 输出：/home/user/example.txt

#b. 获取绝对路径
from pathlib import Path
p = Path("example.txt")
abs_path = p.resolve()
print(abs_path)

####6. 文件遍历####
    #iterdir()：遍历目录内容，生成目录项的 Path 对象。
    #glob(pattern)：按指定模式匹配目录下的文件（非递归）。
    #rglob(pattern)：递归匹配所有子目录和文件
from pathlib import Path
p = Path("D:\\74r1k\pylearn")
pathobj = p.rglob("*")
for path in pathobj:
    print(path)


# 列出目录内容
for item in p.iterdir():
    print(item)

# 使用 glob 匹配
for txt_file in p.glob("*.txt"):
    print(txt_file)

# 使用 rglob 递归匹配
for txt_file in p.rglob("*.txt"):
    print(txt_file)


#7. 路径合并与拆分
#with_name(new_name)：将文件名更改为 new_name，但保持路径不变。
#with_suffix(new_suffix)：将文件扩展名更改为 new_suffix
from pathlib import Path
p = Path("/home/user/example.txt")
new_p = p.with_name("new_example.txt")
new_suffix_p = p.with_suffix(".md")
print(new_p)         # 输出：/home/user/new_example.txt
print(new_suffix_p)  # 输出：/home/user/example.md


####8. 文件权限和属性####
#stat()：获取文件的详细信息，如大小、权限、修改时间等。
#chmod(mode)：更改文件权限
from pathlib import Path
p = Path("example.txt")
file_info = p.stat()
print(file_info.st_size)  # 文件大小
p.chmod(0o755)            # 更改权限
"""
###################################################################
###################################################################
"""
#shutil模块提供了高级文件操作功能，尤其适用于文件和目录的复制、移动、删除，以及管理文件系统操作。
#与 os 模块提供的低级操作不同，shutil 提供了便捷的高级 API

####1. 复制文件和目录####

#a. shutil.copy(src, dst)
#将文件从 src 复制到 dst。如果 dst 是一个目录，则会将文件复制到该目录内

import shutil
shutil.copy("example.txt", "example_copy.txt")
shutil.copy("example.txt", "D:\\74r1k\\pylearn\\5-python文件IO\\example_copy_2.txt")

#b. shutil.copy2(src, dst)  
#与 copy() 类似，但会复制文件的元数据（如时间戳、权限等）
shutil.copy2("source.txt", "destination.txt")  # 复制文件和元数据

#c. shutil.copyfile(src, dst)
#复制文件内容，不复制权限和元数据。dst 必须是一个文件路径，而不是目录
shutil.copyfile("source.txt", "destination.txt")

#d. shutil.copytree(src, dst, dirs_exist_ok=False)
#递归复制整个目录树。dirs_exist_ok=True 表示如果目标目录已存在，不会报错

shutil.copytree("src_folder", "dst_folder")
shutil.copytree("src_folder", "existing_folder", dirs_exist_ok=True)  # 如果目录已存在

####2. 移动文件和目录####
#shutil.move(src, dst)
#将文件或目录从 src 移动到 dst，类似于剪切粘贴。dst 可以是一个目录或文件名
shutil.move("source.txt", "new_location.txt")
shutil.move("folder", "/new/path/folder")  # 移动整个目录

####3. 删除文件和目录####
#shutil.rmtree(path)
#递归删除目录及其所有内容。危险操作，请小心使用，因为会删除整个目录树
shutil.rmtree("folder_to_delete")

####4. 创建压缩文件####
#shutil 提供了生成压缩文件的方法，支持 ZIP、TAR、GZ 等格式
#shutil.make_archive(base_name, format, root_dir)
#创建压缩文件。例如，将整个目录压缩成一个 ZIP 文件。

#base_name：压缩文件的名称（不含扩展名）。
#format：压缩文件格式，支持 zip、tar、gztar、bztar。
#root_dir：要压缩的目录
import shutil
shutil.make_archive("backup", "zip", "archive_test")  # 生成 backup.zip

####5. 解压缩文件####
#对于解压缩，shutil 本身不直接提供方法，但可以通过 shutil.unpack_archive() 进行解压
#shutil.unpack_archive(filename, extract_dir)
#filename：压缩文件的路径。
#extract_dir：解压缩目标目录
import shutil
shutil.unpack_archive("backup.zip", "extracted_folder")  # 解压 backup.zip 到 extracted_folder
"""
##################################################################
##################################################################
""""
# csv 模块用于读写 CSV（逗号分隔值）文件，提供了非常简单和直观的 API 来处理 CSV 数据

####读取 CSV 文件####
import csv
with open("test.csv", mode="r", newline='', encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # 每一行是一个列表

#newline=''：确保跨平台一致的换行处理。
#encoding="utf-8"：处理不同的文件编码，避免出现编码错误

#---------
#DictReader 将每一行数据作为一个字典，字段名对应 CSV 文件的首行,处理表格
import csv
with open("test.csv", mode="r", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # 每一行是一个字典


####3. 写入 CSV 文件####
with open("output.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])       # 写入表头
    writer.writerow(["Alice", 30, "New York"])     # 写入一行
    writer.writerow(["Bob", 25, "Los Angeles"])    # 写入另一行

#---------
with open("output.csv", mode="w", newline='', encoding="utf-8") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # 写入表头
    writer.writerow({"Name": "Alice", "Age": 30, "City": "New York"})
    writer.writerow({"Name": "Bob", "Age": 25, "City": "Los Angeles"})

"""

################################################################
################################################################
#configparser 是 Python 标准库中的一个模块，用于读取和写入配置文件（通常是 .ini 格式）

# 配置文件格式，类似MySQL 的 INI 格式
    #配置文件由多个**节（section）**组成，每个节的内容以 [section_name] 开头。
    #每个节下包含多个键值对（key-value pairs），每对用 = 或 : 分隔。

""" 
[general]
name = MyApp
version = 1.0

[database]
host = localhost
port = 3306
user = admin
password = secret 
"""

####读取配置文件####
"""
#a. 加载配置文件
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


#b. 获取配置值
# 获取指定节下的键值
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
name = config.get("general", "name")
version = config.get("general", "version")
print(f"Name: {name}, Version: {version}")
# 获取数据库配置信息
host = config.get("database", "host")
port = config.getint("database", "port")  # 获取整数值
print(f"'Host': {host}, 'Port': {port}")


####修改配置文件####

#修改现有配置项,使用 set() 方法修改指定节中的键值
# 修改现有键值
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
config.set("general", "version", "1.1")
config.set("database", "password", "new_secret")
config.write(open("config.ini", "w"))  # 写入到配置文件

#b. 添加新的节和键值
# 添加新的节
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
config.add_section("logging")
# 向新节添加键值对
config.set("logging", "level", "debug")
config.set("logging", "file", "/var/log/myapp.log")
config.write(open("config.ini", "w"))  # 写入到配置文件

####使用默认值####
#如果某些键不存在，可以使用 fallback 参数提供默认值

# 如果配置文件中没有 "name" 键，则使用默认值 "DefaultApp"
name = config.get("general", "name", fallback="DefaultApp")
print(f"App Name: {name}")


#####配置文件格式化和注释####
#configparser 模块会自动处理注释（以 # 或 ; 开头的行）并忽略它们

#####完整的demo####
import configparser

# 创建 ConfigParser 实例
config = configparser.ConfigParser()

# 读取配置文件
config.read("config.ini")

# 获取配置项
name = config.get("general", "name")
version = config.get("general", "version")
print(f"App Name: {name}, Version: {version}")

# 获取数据库信息
host = config.get("database", "host")
port = config.getint("database", "port")
print(f"Database Host: {host}, Port: {port}")

# 修改现有配置
config.set("general", "version", "1.1")
config.set("database", "password", "new_secret")

# 添加新的节和键
config.add_section("logging")
config.set("logging", "level", "debug")
config.set("logging", "file", "/var/log/myapp.log")

# 保存修改后的配置
with open("config.ini", "w") as configfile:
    config.write(configfile)

# 输出修改后的文件内容
print("\nUpdated configuration file:")
with open("config.ini", "r") as f:
    print(f.read())

"""
################################################################
################################################################
"""
#序列化和反序列化
#序列化是将对象转换为可存储或传输的格式，而反序列化是将这种格式还原为原始对象

#--------------------JSON 序列化与反序列化--------------------#
#JSON（JavaScript Object Notation）是一种轻量级的数据交换格式

#a. 序列化（Python 对象转为 JSON 格式）
#json.dumps() 方法将 Python 对象转换为 JSON 字符串

import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

json_str = json.dumps(data)
print(json_str)

#可选参数：
    #indent：指定缩进级别，使输出更易读。
    #ensure_ascii：如果为 True，则所有非 ASCII 字符会转义为 Unicode 格式

json_data = json.dumps(data, indent=4)  # 美化输出
print(json_data)


#反序列化（JSON 格式转为 Python 对象）
# 将 JSON 字符串转换为 Python 对象

python_data = json.loads(json_data)
print(python_data)

#--------------------pickle 序列化与反序列化--------------------#
#Pickle 是 Python 自带的用于序列化和反序列化对象的模块
#与 JSON 不同，Pickle 更加灵活，但它不是跨语言的

#a. 序列化（Python 对象转为二进制）
#使用 pickle.dump() 或 pickle.dumps() 方法将 Python 对象转换为二进制数据。
#pickle.dump()：将 Python 对象序列化并直接写入到文件。
#pickle.dumps()：将 Python 对象序列化为字节流（而不是写入文件）

import pickle

# 创建一个 Python 对象（字典）
data = {"name": "John", "age": 30, "city": "New York"}

# 将对象序列化到文件
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

# 或者将对象序列化为字节流
byte_data = pickle.dumps(data)
print(byte_data)

#b. 反序列化（将二进制数据转换为 Python 对象）
#pickle.load()：从文件中读取并反序列化对象。
#pickle.loads()：从字节流中反序列化对象。

# 从文件中加载对象
import pickle
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
print(loaded_data)

# 或者从字节流中反序列化
loaded_data_from_bytes = pickle.loads(byte_data)
print(loaded_data_from_bytes)
"""
##############################################################



