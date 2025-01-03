# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : 列表-for.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/3 14:31 
    @NowThing: 列表-for
"""

from timeit import timeit

lst = [i for i in range(100)]


def with_for():
    max_num = 0
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num


def without_for():
    return max(lst)


def judge_num():
    for num in lst:
        if num > 50:
            return num


def judge_num_func():
    return any(num > 50 for num in lst)


class getTime:
    func = None

    # 求最大值
    @staticmethod
    def getTimeFunc(self, func):
        self.func = func
        return timeit(func, number=1000)

    # 求某个大于50的数值
    @staticmethod
    def getMaxNumFunc(self, func):
        self.func = func
        return timeit(func, number=1000)


print(getTime.getTimeFunc(getTime, with_for))
# 0.001625500000000002
print(getTime.getTimeFunc(getTime, without_for))
# 0.0006412000000000015

print(getTime.getTimeFunc(getTime, judge_num))
# 0.0006073000000000051
print(getTime.getTimeFunc(getTime, judge_num_func))
# 0.0014073999999999892