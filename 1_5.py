vir = float(input("Введите выручку:"))
izd = float(input("Введите издержки:"))
if vir > izd:
    print("Поздравляю! У Вас прибыль!")
    prb = vir - izd
    ren = prb / vir
    print("Ваша рентабельность выручки - {:2.0%}".format(ren))
    sotrud = float(input("Введите количество сотрудников:"))
    print("Прибыль фирмы в расчете на одного сотрудника - {:2.2f}".format(prb / sotrud), "рублей")

else:
    print("Осторожно! У Вас нет прибыли или убыток!")
