def my_func(x, y):
    if x == 0:
        return "Делить на ноль нельзя!"
    else:
        return 1 / (x ** (y * (-1)))


print("Ответ: ", my_func(float(input("Введите x:")), int(input("Введите y:"))))
