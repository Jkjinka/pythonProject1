from random import randint
from functools import reduce


def my_func(a, b):
    return a * b


my_list = [randint(100, 1000) for a in range(0, 4)]
print("Cписок: ", my_list)

print("Произведение всех элементов списка: ", reduce(my_func, my_list))
