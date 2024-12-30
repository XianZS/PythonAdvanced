# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : FilePy13.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/29 23:03 
    @NowThing: 符合设计模式
"""

from abc import ABCMeta, abstractmethod


class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        """ implement in child class """

