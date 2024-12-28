# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : FilePy12.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/28 13:35 
    @NowThing: 单例模式
"""


# https://www.cnblogs.com/wozijisun/p/16635365.html

# 通过装饰器实现单例模式
def MyInstances(cls):
    _instance: dict = {}

    def judge(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance.get(cls)

    return judge


@MyInstances
class stu:
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu1 = stu("jom", 20)
stu2 = stu("kom", 34)
stu3 = stu("lom", 15)
print(stu1)
print(stu2)
print(stu3)
# 先执行装饰器 MyInstances ，将传入参数传给装饰器中的 function : judge 函数，然后进行判断，传给 cls
