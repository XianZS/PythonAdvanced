# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : FilePy11.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/23 09:03 
    @NowThing: 代理设计模式
"""
from abc import ABCMeta,abstractmethod

# 抽象层
"""
    此处定义两个抽象接口
    * IPerson 接口
    * IDo 接口
"""

class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def say_something(self):
        """ say_something """


class IDo(metaclass=ABCMeta):
    @abstractmethod
    def do_something(self):
        """ do_something """

class Person(IPerson,IDo):
    def say_something(self):
        print("say_something")
    def do_something(self):
        print("do_something")

# 接口层
"""
    通过继承抽象接口，实现抽象接口的方法
    IAll
"""
class IAll(IPerson,IDo):
    def __init__(self):
        self.person = Person()
    def say_something(self):
        self.person.say_something()
    def do_something(self):
        self.person.do_something()
someone=IAll()
someone.say_something()
someone.do_something()


