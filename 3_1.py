def func_del(a, b):
    if b == 0:
        return "Делить на ноль нельзя!"
    else:
        return a / b


print(func_del(float(input("Введите числитель:")), float(input("Введите знаменатель:"))))
