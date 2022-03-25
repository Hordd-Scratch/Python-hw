# OOP

from abc import ABC


class Abstractclass(ABC):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # __init__
    # __doc__ документаци
    # __name__ имя класса строкой
    # __bases__ объект класса родителя
    def __del__(self):
        print('i was not deleted')

    # __dict__ словаря со всеми атрибутами (он автоматический)
    # __slots__ если определен то __dict__а не будет

    @classmethod
    def func1(cls, w):
        return 4 * cls * w

    def func2(self, q):
        return 4 * q * self.first

    @property
    def func3(self):
        return 4 * self.first

    @func3.setter
    def func3(self, dat):
        self.first = dat

    @func3.deleter
    def func3(self, dat):
        self.first = 0


a = Abstractclass(12, 34)

print(a.func2(2))
print(a.last)
