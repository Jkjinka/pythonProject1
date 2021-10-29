def my_func(my_list):  # функция подсчета суммы
    my_list2 = []
    for a in my_list:
        if a == "s":  # добавляю условие чтобы посчитать все числа до s
            print("Программа остановлена")
            break
        else:
            try:
                my_list2.append(float(a))
            except ValueError:
                print(f"Слово {a} было исключено из строки!")
    summa = sum(my_list2)
    return summa


def my_func2(my_list):  # функция проверки на остановку
    w = 0
    for a in my_list:
        if a == "s":
            w = 1
    return w


summa1 = 0
q = 0
print("если хотите остановить ввод цифр - введите 's'!")
print(" ")
while q == 0:
    m = input("Введите числа через пробел: ")
    my_list = m.split()
    q = my_func2(my_list)
    summa1 = summa1 + my_func(my_list)
    print(f"сумма всех введеных чисел: {summa1}")
    print(" ")
