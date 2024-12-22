# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : FilePy9.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/22 12:14 
    @NowThing: 类型提示
"""
from mypyc.ir.rtypes import list_rprimitive

"""
    debug 模式 : pip install mypy
"""


def myfunction(my_parameter: int):
    print(my_parameter)


def func1(some: str) -> list:
    print(list(some))
    return list(some)

myfunction(1)
func1("234")