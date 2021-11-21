from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def count(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def count(self):
        return self.v / 6.5 + 0.5


class Kostum(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def count(self):
        return 2 * self.h + 0.3

def count_sum(b, c):
    return b.count + c.count

b = Kostum(5)
c = Coat(10)
print(count_sum(b, c))
