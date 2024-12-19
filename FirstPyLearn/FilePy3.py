# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced
    @File    : FilePy3.py
    @IDE     : PyCharm
    @Author  : XianZS
    @Date    : 2024/12/2 11:46
    @NowThing: 基于装饰器实现的 log 记录功能
"""


def logged(function):
    def wrapper(*args, **kwargs):
        # 得到返回参数
        value = function(*args, **kwargs)
        with open("LogFile.txt", "a+") as f:
            f_name = function.__name__
            print(f"{f_name} ran with args: {args}, and kwargs: {kwargs},{value}\n")
            f.write(f"{f_name} ran with args: {args}, and kwargs: {kwargs}\n")
        return value

    return wrapper


@logged
def add(x: int, y: int) -> int:
    return x + y


if __name__ == '__main__':
    add(30, 10)
