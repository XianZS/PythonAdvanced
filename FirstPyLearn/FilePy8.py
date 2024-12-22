# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : FilePy8.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/22 10:46 
    @NowThing: 封装
    https://www.runoob.com/python/python-func-property.html
"""
"""
    property函数字如其名，其在装饰器的主要应用在于，
    我们要实现保护类的封装特性，让开发者可以使用“对象.属性”的方式操作操作类属性
"""


class Person:
    def __init__(self, name, age, gender, address):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.address = address

    @property
    def Name(self):
        # property() : 函数的作用是在新式类中返回属性值。
        # property() : 函数是用来创建一个托管属性，对类中定义的属性进行托管操作的。
        return self.__name

    @Name.setter
    # 设置
    def Name(self, value):
        self.__name = value

    @Name.deleter
    # 删除
    def Name(self):
        del self.__name

    @Name.getter
    # 得到
    def Name(self):
        return self.__name

    @staticmethod
    # 静态方法
    def hello():
        print("Hello World!")


if __name__ == '__main__':
    person = Person("jom", 18, "男", "ShangHai")
    print(person.Name)
    Person.hello()
    print(person.hello())