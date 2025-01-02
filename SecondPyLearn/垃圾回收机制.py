# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : 垃圾回收机制.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/2 09:20 
    @NowThing: 垃圾回收
"""

import gc


class TreeNode:
    def __init__(self, parent=None):
        self.left = None
        self.right = None
        self.parent = parent


node1 = TreeNode()
node2 = TreeNode(parent=node1)
# 循环引用
node1.left = node2

del node1
del node2

if __name__ == '__main__':
    print(f"Unreachable Objects: {gc.collect()}")
