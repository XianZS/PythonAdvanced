# -*- coding: UTF-8 -*-
"""
    @Project : PythonAdvanced 
    @File    : FilePy7.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2024/12/19 09:16 
    @NowThing: 
"""
import sys
# python 标准库之的 getopt 模块
import getopt

# 获取命令行的参数
"""
    getopt.getopt(sys.argv[1:],"参数key1:参数key2:……:参数keyn:",)
"""


def main():
    opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["filename", "message"])
    print(opts)
    print(args)


filename = ""
message = ""


def writeMessage():
    global message
    global filename
    opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["filename", "message"])
    for opt, arg in opts:
        if opt == "-f":
            filename = opt
        if opt == "-m":
            message = arg
    with open(filename, "a+") as f:
        f.write(message + "\n")


if __name__ == '__main__':
    writeMessage()
