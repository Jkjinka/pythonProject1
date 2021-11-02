from itertools import count
from itertools import cycle

print("***ПЕРВЫЙ СКРИПТ***")
a = int(input("Ввведите число с которого начнем: "))
n = int(input("Введите шаг между числами: "))
m = int(input("Введите максимальное число: "))
print("Полученная последовательность: ")
for el in count(a, n):
    if el > m:
        break
    else:
        print(el)
print(" ")
print("***ВТОРОЙ СКРИПТ***")
my_list = ["A", "B", "C"]
c = cycle(my_list)
d = int(input("Введите сколько раз повторить все элементы списка: "))
j = len(my_list) * d
for i in range(0, j):
    print(next(c))
