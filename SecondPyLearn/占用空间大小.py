# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : 占用空间大小.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/2 14:12 
    @NowThing: 占用空间大小
"""
import sys
from abc import ABCMeta, abstractmethod

# python ——》 字节码 ——》 C语言虚拟机运行

print(sys.getsizeof([0] * 3))
# 80
print(sys.getsizeof([0, 0, 0]))
# 80
print(sys.getsizeof([0 for _ in range(3)]))
# 88
