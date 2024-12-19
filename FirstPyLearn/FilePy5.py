# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : FilePy5.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/17 13:55 
    @NowThing: 
"""
def myFunction(*args,**kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(kwargs["KeyOne"])
    print(kwargs["KeyTwo"])
    print("args",args)
    print("kwargs",kwargs)

# 位置实参位于关键字实参的前面
# myFunction(位置实参，关键字实参)
myFunction("hey",True,"hello",KeyOne="keyOne",KeyTwo="keyTwo")
