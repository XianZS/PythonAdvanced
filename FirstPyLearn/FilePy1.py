class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 代码执行完毕后，自动调用
    def __del__(self):
        print("Object destroyed")


p1 = Person("John", 25)


class Vector:
    """
    在这里python并不知道什么叫做向量，只知道有两个属性，x和y
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 添加 __add__ 表示在当前类中定义了 + 运算符的操作行为
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        # 当我们进行类型转换时会输出，直接 str
        return f"x: {self.x}, y: {self.y}"

    def __repr__(self):
        # 当我们直接输出对象时会输出，直接 print
        return f"x: {self.x}, y: {self.y}"

    def __len__(self):
        # 当我们进行 len 操作时，直接 len
        return self.x * self.y

    def __call__(self, a):
        # __call__ 方法主要提供的功能是让一个对象实例还能够像函数一样调用。
        print("call")


v1 = Vector(1, 2)
v2 = Vector(3, 4)
# 如果直接对其进行 + 运算，会得到错误提示
v3 = v1 + v2
print(v3.x, v3.y)
print(str(v3))
print(len(v3))
print(v3("some"))
