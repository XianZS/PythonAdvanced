# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : FilePy4.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/2 11:54 
    @NowThing: 基于装饰器实现的“想知道一个函数的执行时间”
"""

import time


def timed(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = function(*args, **kwargs)
        end = time.time()
        with open("LogFile.txt", "a+") as f:
            f.write(function.__name__ + " : " + str(end - start) + "\n")
        return res

    return wrapper


@timed
def my_func(n):
    for i in range(n):
        time.sleep(0.1)
    return "my_func"


print(my_func(10))
# my_func's print is 'my_func ran in 1.087409257888794s'.
