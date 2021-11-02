from sys import argv

script_name, a, b, c = argv
a = int(a)
b = int(b)
c = int(c)
s = (a * b) + c
print("выработка в часах: ", a)
print("Ставка в час: ", b)
print("Премия: ", c)
print("Зарплата: ", s)
