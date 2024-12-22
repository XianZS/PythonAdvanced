# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : FilePy10.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/22 15:01 
    @NowThing: 工厂模式 --- 工厂函数
"""
"""
    增加模块化的思想
    防止违反 “开放封闭原则”
    虽然减少了代码的耦合性，但是也增加了代码的抽象性
    工厂方法模式的特点：
        * 定义一个接口来创建对象，但工厂本身并不负责创建动作，而是由其子类决定实例化哪些类
        * 工厂方法的创建是通过继承而不是通过实例化来完成的
        * 工厂方法使设计更具有定制性。可以返回相同的实例或子类
    一个工厂只能生产一种产品 ——————》 一个工厂可以生产多种产品
"""

from abc import ABCMeta, abstractmethod


# 在 python 中接口类的命名方式一般以 I 开头
class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method(self):
        pass


class Student(IPerson):
    def __init__(self, name):
        self.name = name

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):
    def __init__(self, name):
        self.name = name

    def person_method(self):
        print("I am a teacher")


if __name__ == '__main__':
    s1 = Student("jom")
    s1.person_method()
    t1 = Teacher("kom")
    t1.person_method()
