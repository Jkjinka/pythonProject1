def int_func(a):
    n = 0
    for b in a:
        if n == 0:
            с = b.upper()
            n = n + 1
        else:
            с = с + b

    return с


# первая часть задачи
m = input("Введите слово в нижнем регистре: ")
print(f"Исправленное слово: {int_func(m)}")
print(" ")
# вторая часть задачи
str1 = input("Введите строку в нижнем регистре: ")
my_list = str1.split()
n = 0
for a in my_list:
    if n == 0:
        str2 = int_func(a)
        n = n + 1
    else:
        str2 = str2 + " " + int_func(a)

print(f"Исправленная строка: {str2}")
