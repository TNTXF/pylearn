#python exceptions
########################################################################
"""
#异常处理
#Python 使用 try、except、else 和 finally 语句来处理异常
try:
    # 可能发生异常的代码
    result = 10 / 0
except ZeroDivisionError as e:
    # 处理特定异常
    print("除数不能为零:", e)
except Exception as e:
    # 捕获其他异常
    print("发生异常:", e)
else:
    # 当没有异常发生时执行
    print("操作成功:", result)
finally:
    # 无论是否发生异常都会执行
    print("执行完毕")


#自定义异常
#有时内置的异常不足以描述特定的错误，可以自定义异常
class CustomError(Exception):
    #自定义异常
    pass

def check_positive(value):
    if value < 0:
        raise CustomError("值必须为正数")
    return value

try:
    check_positive(-10)
except CustomError as e:
    print("捕获自定义异常:", e)

#异常的传播
#异常会在程序栈中向上传播，直到找到合适的 except 处理代码，或者到达顶层引发未处理的异常
def level1():
    level2()

def level2():
    raise ValueError("来自 level2 的异常")

try:
    level1()
except ValueError as e:
    print("捕获异常:", e)

#使用 with 语句的异常处理
#with 语句结合上下文管理器，可以简化资源的释放
try:
    with open("file.txt", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print("文件未找到:", e)

"""
########################################################################
"""
#Python 模块
#模块 (Module) 是一个包含 Python 定义和语句的文件，文件名以 .py 结尾。
#模块的名称就是文件名去掉 .py 的部分，可以通过 import 导入模块

####导入模块的方式####

#import 导入整个模块
import math  #math是.py文件，ctrl+点击可以查看源码
print(math.sqrt(16))  # 调用 math 模块中的 sqrt 函数

#from...import... 导入模块中的特定对象
from math import sqrt # sqrt 是一个函数，ctrl+点击可以查看源码
print(sqrt(16))  # 直接使用 sqrt


#from...import... as 别名
#给导入的模块或对象设置别名，以简化调用或避免命名冲突
import math as m
print(m.sqrt(16))

from math import sqrt as s
print(s(16))

#导入模块中的所有对象
#使用 from module_name import * 导入模块中的所有对象。通常不建议这样使用，以避免命名冲突

from math import *
print(sqrt(16))


####创建和使用自定义模块####
# 文件: my_module.py

def greet(name):
    return f"Hello, {name}!"

pi = 3.14159

#然后在其他文件中导入使用
import my_module

print(my_module.greet("Alice"))
print(my_module.pi)
"""
####Python 内置模块####
#os：用于操作系统相关功能，如文件和目录管理
#sys：提供与 Python 解释器相关的功能，如处理命令行参数、退出程序等
#datetime：处理日期和时间。
#math：提供数学运算函数，如幂运算、对数、三角函数等。
#random：生成随机数和随机选择
#json：用于处理 JSON 数据格式

####包 (Package)####
#包是一种组织模块的方式，通常是一个包含 __init__.py 文件的文件夹，可以包含多个模块
#包可以帮助分层管理大型项目中的模块

#在 Python 包中，__init__.py 文件是包的初始化文件，用于标识该目录是一个 Python 包
#标识文件夹为包
    #在 Python 中，包就是一个包含多个模块的目录，__init__.py 文件表明该目录是一个包。
    #如果目录中没有 __init__.py 文件，那么这个目录不会被识别为一个 Python 包
"""
#初始化包
    #__init__.py 文件可以包含一些初始化代码，比如在包导入时运行的代码。
    #你可以在 __init__.py 文件中定义全局变量、导入子模块，甚至执行一些初始化操作，这样在导入包时这些代码会自动执行

# my_package/__init__.py
print("Initializing my_package")
my_variable = "Hello from my_package"
#当导入 my_package 时，print 语句会被执行，my_variable 也可以在包外直接访问
#import my_package
#print(my_package.my_variable)

# 控制包的导入行为
#可以使用 __init__.py 控制包中的哪些模块会被导入
# my_package/__init__.py
__all__ = ["module1", "module2"]
#这样当执行 from my_package import * 时，只有 module1 和 module2 会被导入

#重构包的结构
# my_package/__init__.py
from .module1 import func1
from .module2 import func2
#这样在包外部使用时，可以直接通过 my_package.func1 和 my_package.func2 访问函数
import my_package
my_package.func1()
my_package.func2()

#空的 __init__.py
#在 Python 3.3 之后，__init__.py 不再是创建包的必需文件（即可以没有 __init__.py 也能识别为包）。
#但出于可读性和兼容性考虑，很多项目仍然会保留空的 __init__.py 文件


#创建包结构：

#my_package/
#├── __init__.py
#├── module1.py
#└── module2.py 

#使用包：通过 import 导入包内的模块或函数
#from my_package import module1
#module1.some_function()

#### 查找模块路径####
#Python 会在指定的路径中查找模块，可以通过 sys.path 查看搜索路径
import sys
print(sys.path)

#要在自定义路径中导入模块，可以将路径添加到 sys.path
import sys
sys.path.append('/path/to/your/module')
import your_module


####使用 __name__ == "__main__" 进行模块测试####
# my_module.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Alice"))  # 仅在直接运行时执行,my_module.py 作为主模块时if不执行
#当直接运行 my_module.py 时，会输出 Hello, Alice；当它被导入时，不会执行 if 语句中的代码
"""

########################################################################
#python的包管理工具

####pip 是 Python 的标准包管理工具

""" 
pip install package_name
pip install package_name==1.0.0
pip install --upgrade package_name
pip uninstall package_name
pip list
pip list --outdated
#将依赖项保存到文件
pip freeze > requirements.txt
pip install -r requirements.txt """

####virtualenv 和 venv
#virtualenv 和 venv 用于创建独立的虚拟环境，使每个项目的依赖独立管理，避免全局包的冲突

#创建虚拟环境: python -m venv env_name
#激活虚拟环境：
# Windows
#env_name\Scripts\activate
# macOS/Linux
#source env_name/bin/activate
#退出虚拟环境:deactivate
#删除虚拟环境：rm -rf env_name

####pipenv 是一个将 pip 和 virtualenv 集成到一起的工具

####Poetry 是一种新的依赖管理工具，提供包管理和发布功能，它特别适用于创建和发布 Python 包

####Conda 是一个跨平台的包管理和环境管理工具，适用于 Python 和其他语言

########################################################################
#python插件化开发

#插件化开发的基本原理
#在插件化架构中，核心应用程序（主程序）和插件之间通常有一个明确的协议或接口。
#插件可以动态加载到应用程序中，应用程序调用插件中的功能而无需直接依赖插件的实现细节

#插件化开发的核心组成部分：
    #主程序：管理插件加载和执行的主体，定义插件接口或规范。
    #插件接口：一个插件必须遵循的协议或 API，使得主程序能够正确识别和调用插件。
    #插件（Module）：实现具体功能的模块，符合主程序的接口协议，通常在运行时动态加载

#使用 Python 的插件化开发方法
#使用 entry points 实现插件化（推荐）
#Python 包管理工具 setuptools 提供了 entry points 机制，使得开发者可以注册插件，主程序可以通过 entry points 动态加载插件
"""
#定义主程序接口
# myapp/plugin_interface.py
class PluginInterface:
    def execute(self):
        pass

#定义插件并配置 entry point
#编写插件，并在 setup.py 中注册插件的 entry point：
# hello_plugin/hello_plugin.py
#from myapp.plugin_interface import PluginInterface

class HelloPlugin(PluginInterface):
    def execute(self):
        print("Hello from HelloPlugin!")

# setup.py
from setuptools import setup, find_packages

setup(
    name="hello_plugin",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "myapp.plugins": [
            "hello = hello_plugin:HelloPlugin"
        ]
    },
)

#主程序加载插件
# myapp/main.py
import importlib.metadata
#使用 pkg_resources 模块或 importlib.metadata 加载所有注册在 myapp.plugins 下的插件
def load_plugins():
    plugins = []
    for entry_point in importlib.metadata.entry_points().get("myapp.plugins", []):
        plugin_class = entry_point.load()
        plugins.append(plugin_class())
    return plugins

plugins = load_plugins()
for plugin in plugins:
    plugin.execute()

#安装和使用插件
#安装插件时，entry points 会被注册到系统，主程序可以直接使用
"""
################################################################
