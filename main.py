from abc import ABCMeta, abstractmethod,ABC

class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def say_something(self,some):
        """ say hello """
        pass

class S1(IPerson):
    def say_something(self,some):
        print(some)

s1=S1()
s1.say_something("hello")