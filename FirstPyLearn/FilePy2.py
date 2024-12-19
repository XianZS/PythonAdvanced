"""
    装饰器
"""


def my_decorator1(func):
    # 装饰器的包装函数，参数类型为引用变量
    def wrapper():
        print("这是一个修饰器")
        # 调用 func ， func 是被修饰的函数，参数类型为引用变量
        func()

    return wrapper


def hello1():
    print("hello")


def my_decorator2(func):
    # 装饰器的包装函数，参数类型为引用变量
    def wrapper():
        print("这是一个修饰器")
        # 调用 func ， func 是被修饰的函数，参数类型为引用变量
        func()

    return wrapper


@my_decorator2
def hello2():
    print("hello2")


def my_decorator3(func):
    # 存在传入参数
    def wrapper(*args, **kwargs):
        print("带传入参数的装饰器")
        func(*args, **kwargs)

    return wrapper


@my_decorator3
def hello3(person):
    print(f"hello {person}")


def my_decorator4(func):
    def wrapper(*args, **kwargs):
        return_something = func(*args, **kwargs)
        print("带返回值的装饰器")
        return return_something

    return wrapper


@my_decorator4
def hello4(person):
    print("Now running hello4 func that return something")
    return f"hello {person}"


if __name__ == '__main__':
    # 调用 my_decorator 函数，参数类型为引用变量
    # 这只是装饰器内部的想法，实际上并不这样操作，因为装饰器存在“语法糖”
    my_decorator1(hello1)()
    print("*" * 30)
    # 如下是正确的调用方式，使用了“语法糖”
    hello2()
    print("*" * 30)
    hello3("Mike")
    print("*" * 30)
    print(hello4("Mike"))
