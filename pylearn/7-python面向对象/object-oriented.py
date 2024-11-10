#面向对象编程（OOP）是通过类和对象来组织和管理代码的一种编程方式
"""
####类和对象####
#类（Class）：是对具有相似属性和行为的对象的抽象，可以看作是对象的蓝图。
#对象（Object）：类的实例化结果，通过类创建的具体存在

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating.")

dog = Animal("Buddy", 5)
print(dog.name)  # Buddy

dog.eat()  # Buddy is eating.

####__init__ 方法（构造函数）####
#__init__ 是 Python 的构造函数，在创建对象时自动调用，用于初始化对象的属性

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


#### 属性和方法####
#属性：类或对象的数据，通过 self 访问，分为类属性和实例属性。
#方法：类或对象的行为，定义在类内部的函数，通常带有 self 参数

class Dog:
    species = "Canine"  # 类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age

    def bark(self):  # 实例方法
        print(f"{self.name} is barking")


####封装#####
#封装是将属性和方法保护起来，只允许通过类的内部来访问，从而保证数据的安全性

#私有属性：在属性名前加下划线 _ 或 __，通常代表内部属性。
#访问器（getter）和修改器（setter）：提供方法来访问和修改私有属性。

class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

dog = Dog("Buddy", 5)
print(dog.get_name())
dog.set_name("Max")
print(dog.get_name())  # Max


#### 继承####
#继承是指一个类可以从另一个类中继承属性和方法，这样可以实现代码复用
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f"Animal is speaking")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

dog = Dog("Buddy", 5)
dog.speak()  # Buddy says Woof!

#多重继承
class Animal:
    pass

class Canine:
    pass

class Dog(Animal, Canine):  # 多重继承
    pass


####多态####
#多态允许不同的子类在调用相同方法时，表现出不同的行为。在 Python 中，多态通过方法的重写来实现
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()  # 输出 "Woof!" 和 "Meow!"


####抽象类和接口####
#Python 中通过 abc 模块来定义抽象类，抽象类不能直接实例化，必须被子类继承并实现抽象方法

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()  # 输出: Woof!
#下面会报错
annimal = Animal()
annimal.speak() 


####特殊方法和运算符重载####
#特殊方法（又称“魔法方法”）是以双下划线开头和结尾的，比如 __init__、__str__、__repr__
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # 重载加法运算符
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1 + v2)  # 输出: (7, 10)


####类方法和静态方法####
#类方法：使用 @classmethod 装饰器定义，以 cls 作为第一个参数，适用于类级别的操作。
#静态方法：使用 @staticmethod 装饰器定义，不需要 self 或 cls 参数，适用于独立于实例或类的功能。

class MyClass:
    class_attribute = 0

    @classmethod
    def class_method(cls):
        cls.class_attribute += 1
        print(cls.class_attribute)

    @staticmethod
    def static_method():
        print("This is a static method.")

MyClass.class_method()   # 输出: 1
MyClass.static_method()  # 输出: This is a static method.


####属性装饰器 @property####
#@property 用于将方法转化为只读属性，@property.setter 用于定义可修改属性。常用于封装私有属性

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):  # 读取属性
        return self._temperature

    @temperature.setter
    def temperature(self, value):  # 设置属性
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

temp = Celsius()
temp.temperature = 25  # 设置属性
print(temp.temperature)  # 输出: 25
"""

#######################python特殊属性详解##################################
"""
#__dict__ 是一个字典，包含了类或对象的所有可访问属性和它们对应的值
#通过 __dict__ 可以动态地获取和修改对象的属性

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog = Dog("Buddy", 5)
print(dog.__dict__)  # 输出: {'name': 'Buddy', 'age': 5}

dog.__dict__['color'] = "black"  # 动态添加属性
print(dog.__dict__) #


#__class__ 是对象所属的类，通过 __class__ 可以查看实例的类信息
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog = Dog("Buddy",3)
print(dog.__class__)  # 输出: <class '__main__.Dog'>

#__name__
#在模块中，__name__ 用于表示模块名。如果模块被直接运行，则 __name__ 的值为 __main__；如果模块被导入，则 __name__ 的值为模块的名字。
#在类中，__name__ 表示类名

#__module__
#__module__ 表示类定义所在的模块名称。如果类是在当前模块定义的，则 __module__ 的值为 __main__；否则为模块名称
print(Dog.__module__)

#__doc__
#__doc__ 用于获取类、函数或模块的文档字符串（Docstring）

class Dog:
    """This is a Dog class."""

print(Dog.__doc__)  # 输出: This is a Dog class.


#__bases__
#__bases__ 表示类的直接基类构成的元组。通过 __bases__ 可以查看类的继承关系
class Animal:
    pass

class Dog(Animal):
    pass

print(Dog.__bases__)  # 输出: (<class '__main__.Animal'>,)

#__mro__
#__mro__（方法解析顺序）是一个元组，表示类的继承顺序。对于多重继承的类，这个属性用于确定方法的调用顺序
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.__mro__)  # 输出: (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

#__slots__
#__slots__ 限制类的属性，避免创建 __dict__，从而节省内存
#__slots__ 定义一个类可以拥有的属性名称列表，使得对象只能包含特定的属性

class Dog:
    __slots__ = ['name', 'age']  # 只允许 'name' 和 'age' 属性

dog = Dog()
dog.name = "Buddy"
dog.age = 3
dog.color = "Brown"  # 会报错，因为 'color' 不在 __slots__ 中

#__file__
#在模块中，__file__ 用于获取模块文件的路径
# 假设在文件 test_module.py 中执行以下代码
print(__file__)  # 输出: 文件的绝对路径或相对路径

#__call__
#如果在类中定义了 __call__ 方法，那么该类的实例可以像函数一样被调用

class Dog:
    def __call__(self, sound):
        print(f"The dog says: {sound}")

dog = Dog()
dog("Woof!")  # 输出: The dog says: Woof!

#__len__
#__len__ 方法用于实现 len() 函数的行为。自定义类可以定义 __len__ 来使 len() 获取对象的长度
class Container:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

container = Container([1, 2, 3, 4])
print(len(container))  # 输出: 4

#__getitem__, __setitem__, __delitem__
#这些方法用于对象的索引操作，使得对象可以像列表或字典一样进行索引访问
class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

my_list = MyList([1, 2, 3])
print(my_list[1])  # 输出: 2
my_list[1] = 5
print(my_list[1])  # 输出: 5
del my_list[1]
print(my_list.items)  # 输出: [1, 3]

#__str__ 和 __repr__
#__str__：用于定义对象的字符串表示，通常用于 print() 或 str() 时调用。
#__repr__：用于定义对象的官方表示，通常用于调试，建议返回一个可以用来重建对象的字符串
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog named {self.name}"

    def __repr__(self):
        return f"Dog('{self.name}')"

dog = Dog("Buddy")
print(str(dog))   # 输出: Dog named Buddy
print(repr(dog))  # 输出: Dog('Buddy')

#__new__
#__new__ 是类的实例创建方法，用于控制对象的创建过程。在实例化对象之前调用，用来分配内存

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # 输出: True

#__enter__ 和 __exit__
#__enter__ 和 __exit__ 方法用于上下文管理器（with 语句），主要用于资源管理，如文件的自动打开和关闭。
class MyResource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")

with MyResource() as resource:
    print("Using resource")
# 输出:
# Resource acquired
# Using resource
# Resource released

#__iter__ 和 __next__
#__iter__：使对象成为一个可迭代对象。
#__next__：定义迭代对象中的每个值，在 for 循环或 next() 函数中被调用。
class MyIterator:
    def __init__(self):
        self.data = [1, 2, 3]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

for item in MyIterator():
    print(item)  # 输出: 1 2 3
"""
################################################################
"""
#Monkey Patch 是一种动态修改类或模块的方法，通常用于在程序运行时更改或扩展已有的代码行为

#临时修复 Bug：在第三方库的代码中发现 Bug 而又不方便修改时，可以使用 Monkey Patch 来修复该库的函数或方法。
#扩展功能：在不改变原始代码的前提下，添加新的方法或修改现有方法以实现更多功能。
#测试和模拟：在测试环境中，可以用 Monkey Patch 替换或修改某些函数的实现，以达到更灵活的测试目的，比如模拟网络请求的响应。

#如何实现 Monkey Patch
# 假设我们有一个模块 module.py
class Animal:
    def speak(self):
        return "I am an animal."

# 使用 Monkey Patch 修改 Animal 的 speak 方法
def new_speak():
    return "I am a patched animal."

Animal.speak = new_speak  # 替换原来的 speak 方法

# 测试效果
animal = Animal()
print(animal.speak())  # 输出: I am a patched animal.

#缺点：
#代码可读性下降：Monkey Patch 的逻辑可能不在类或模块的定义中，增加了理解成本。
#难以维护：随着第三方库更新，Patch 代码可能不再适用，需要不断调整。
#潜在冲突：多个 Monkey Patch 对同一个方法操作可能导致不可预见的问题。

"""
########################运算符重载详解##############################
#可以让类通过实现特殊方法（Magic Methods）来支持运算符（如 +、-、*、/ 等）的自定义行为。
# 通过运算符重载，可以让自定义类像内置类型一样进行操作，这使得代码更具可读性和 Pythonic 风格

#1. 什么是运算符重载
#在 Python 中，运算符（例如 +, -, *, /）是通过调用类中的特殊方法来实现的
#例如，表达式 a + b 实际上是调用 a.__add__(b) 方法


#常见的运算符及其重载方法
"""
运算符  方法名               说明
 +	    __add__	            加法
-	    __sub__	            减法
*	    __mul__	            乘法
/	    __truediv__	        真除法
//	    __floordiv__	    地板除法
%	    __mod__	            取模
**	    __pow__	            幂运算
==	    __eq__	            等于
!=	    __ne__	            不等于
<	    __lt__	            小于
<=	    __le__	            小于等于
>	    __gt__	            大于
>=	    __ge__	            大于等于
[]	    __getitem__	        索引访问
in	    __contains__	    成员检测
()	    __call__	        调用对象
str()	__str__	            字符串表示
repr()	__repr__	        正式表示 

"""
#其他双目运算符
#Python 支持一些双目运算符的反向重载（reverse operator overloads）
#当左操作数不支持该运算符时，调用右操作数的反向方法
"""
正向方法	    反向方法
__add__	        __radd__
__sub__	        __rsub__
__mul__	        __rmul__
__truediv__	    __rtruediv__
__floordiv__	__rfloordiv__
__mod__	        __rmod__
__pow__	        __rpow__
"""
"""
#例如，对于 a + b 表达式，如果 a 不支持 __add__，Python 会调用 b 的 __radd__ 方法
class Value:
    def __init__(self, x):
        self.x = x

    def __radd__(self, other):
        return self.x + other

# 测试
val = Value(10)
print(5 + val)  # 输出: 15
"""
###############################
"""
#运算符重载示例1 ：向量加法
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# 测试
v1 = Vector(2, 4)
v2 = Vector(3, 5)
v3 = v1 + v2
print(v3)  # 输出: Vector(5, 9)

#示例 2：实现比较运算符
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

# 测试
rect1 = Rectangle(3, 4)
rect2 = Rectangle(2, 6)
print(rect1 < rect2)   # 输出: False
print(rect1 <= rect2)  # 输出: True
print(rect1 == rect2)  # 输出: True

"""
################################################################
#反射（Reflection）是一种在运行时检查或修改对象的能力。
#通过反射，可以在不知道对象类型的情况下动态地访问对象的属性、方法，甚至可以动态创建类或修改类的行为

#Python 反射的常用内置函数
""" 
函数	    作用
getattr	    获取对象的属性或方法
setattr	    设置对象的属性值
hasattr	    检查对象是否包含某属性或方法
delattr	    删除对象的属性
type	    获取对象的类型
isinstance	判断对象是否是某类的实例
dir	        列出对象的所有属性和方法 
"""

#getattr - 获取对象的属性或方法
#getattr 可以用于获取对象的属性或方法。如果属性不存在，还可以指定一个默认值来避免抛出异常
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# 创建对象
p = Person("Alice", 30)

# 使用 getattr 获取属性和方法
name = getattr(p, "name")
print(name)  # 输出: Alice

greet_method = getattr(p, "greet")
greet_method()  # 输出: Hello, my name is Alice.

# 获取不存在的属性，并指定默认值
gender = getattr(p, "gender", "Unknown")
print(gender)  # 输出: Unknown

#setattr - 设置对象的属性
#setattr 用于动态设置对象的属性值，即使该属性在类中未定义，也可以通过 setattr 来动态添加
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

# 创建对象
car = Car("Toyota", 2020)

# 使用 setattr 设置属性
setattr(car, "year", 2021)
print(car.year)  # 输出: 2021

# 动态添加新属性
setattr(car, "color", "blue")
print(car.color)  # 输出: blue

#反射的高级应用
#通过反射实现插件系统，允许用户动态地加载和调用模块中的插件
class PluginA:
    def run(self):
        print("Plugin A is running")

class PluginB:
    def run(self):
        print("Plugin B is running")

def load_and_run_plugin(plugin_name):
    plugin_class = globals().get(plugin_name)
    if plugin_class:
        plugin = plugin_class()
        plugin.run()
    else:
        print("Plugin not found")

# 加载并运行插件
load_and_run_plugin("PluginA")  # 输出: Plugin A is running
load_and_run_plugin("PluginB")  # 输出: Plugin B is running
load_and_run_plugin("PluginC") # 输出：Plugin not found

"""
##########################描述器#################################
#描述器（Descriptor） 是一种协议或机制，用于管理对象属性的访问和设置。描述器的本质是对象的属性访问方法
#通过定义描述器，我们可以自定义属性的获取、设置和删除逻辑，从而实现更细粒度的控制
#描述器是 Python 中一个非常强大和灵活的特性，广泛用于 ORM（如 SQLAlchemy）、Django 的模型字段、缓存机制等方面

#1. 什么是描述器
#描述器是一个对象，它通过实现以下任意一个或多个特殊方法来定制属性的行为：
""" 
__get__(self, instance, owner)：获取属性的值。
__set__(self, instance, value)：设置属性的值。
__delete__(self, instance)：删除属性的值。
 """

#描述器的协议
""" 
一个对象成为描述器，需要实现以下至少一个方法：
__get__：用来获取属性的值。
__set__：用来设置属性的值。
__delete__：用来删除属性的值
"""

###__get__ 方法
""" __get__ 用于返回属性值。它接受三个参数：

self：描述器实例。
instance：拥有该属性的对象（如果该属性是实例属性）。
owner：拥有该属性的类。 """

###__set__ 方法
""" __set__ 用于设置属性的值。它接受三个参数：

self：描述器实例。
instance：拥有该属性的对象。
value：要设置的新值。 """

###__delete__ 方法
""" __delete__ 用于删除属性的值。它接受两个参数：

self：描述器实例。
instance：拥有该属性的对象。 """

#####使用描述器####
"""
class MyDescriptor:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        print(f"Getting value: {self.value}")
        return self.value

    def __set__(self, instance, value):
        print(f"Setting value to: {value}")
        self.value = value

    def __delete__(self, instance):
        print(f"Deleting value")
        self.value = None


class MyClass:
    attr = MyDescriptor()


obj = MyClass()
obj.attr = 42  # 设置值
print(obj.attr)  # 获取值
del obj.attr  # 删除值

####示例 2：限制属性值
class RangeDescriptor:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if self.min_value <= value <= self.max_value:
            self.value = value
        else:
            raise ValueError(f"Value must be between {self.min_value} and {self.max_value}")

    def __delete__(self, instance):
        self.value = None


class MyClass:
    age = RangeDescriptor(0, 100)


obj = MyClass()
obj.age = 25  # 合法
print(obj.age)  # 输出: 25
obj.age = 120  # 抛出异常: ValueError: Value must be between 0 and 100

###描述器与 property
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value

    @value.deleter
    def value(self):
        print("Deleting value")
        del self._value


obj = MyClass(10)
print(obj.value)  # 获取值
obj.value = 20  # 设置值
del obj.value  # 删除值
"""
################################################################