class Off_equip:
    def __init__(self, name, model, count):
        self.name = name  # наименование
        self.model = model  # модель
        self.count = count  # цена


    def get_equip(n):  # прием на склад

        if n == "p":
            print("Введите данные:")
            return Printer(input("Наименование: "), input("Модель: "), input("Цена: "), input("Цвет: "))
        if n == "s":
            print("Введите данные:")
            return Scaner(input("Наименование: "), input("Модель: "), input("Цена: "), input("Тип ПО: "))
        if n == "k":
            print("Введите данные:")
            return Kseroks(input("Наименование: "), input("Модель: "), input("Цена: "), input("Формат печати: "))
        print("Введена неправильно категория техники! Повторите ввод!")

    def account(my_dict, my_list):  # учет техники

        n = input("Выберите подразделение (p-Продажники, b-Бухгалтерия): ")
        if n == "p":
            ls = my_dict.get("Продажники")
            ls[1] = ls[1] + 1
            free_list(my_list)
            a = int(input("Выберите технику из списка (укажите порядковый номер): "))
            ls[0] = my_list[a]
            my_dict.update({"Продажники": ls})
            return my_dict
        if n == "b":
            ls = my_dict.get("Бухгалтерия")
            ls[1] = ls[1] + 1
            free_list(my_list)
            a = int(input("Выберите технику из списка (укажите порядковый номер): "))
            ls[0] = my_list[a]
            my_dict.update({"Бухгалтерия": ls})
            return my_dict
        print("Введено неправильно подразделение! Повторите ввод!")


class Printer(Off_equip):
    def __init__(self, name, model, count, color):
        Off_equip.__init__(self, name, model, count)
        self.color = color  # цвет печати
        self.type = "принтер"


class Scaner(Off_equip):
    def __init__(self, name, model, count, soft):
        Off_equip.__init__(self, name, model, count)
        self.soft = soft  # вид ПО
        self.type = "сканер"


class Kseroks(Off_equip):
    def __init__(self, name, model, count, format):
        Off_equip.__init__(self, name, model, count)
        self.format = format  # формат печати
        self.type = "ксерокс"


def free_list(my_list):
    print("Список техники (№, наим, вид):")
    j = 0
    for i in my_list:
        print(f"{j}. {i.name}, {i.type}")
        j = j + 1


my_list = []
my_dict = {"Бухгалтерия": [[], 0], "Продажники": [[], 0]}
# n = input("Выберите тип техники (p-printer, s-scaner, k-kseroks):\n")
i = 0
while i == 0:
    try:
        a = int(input(
            "Выберите интересующую Вас категорию!\n Вы хотите добавить товар? - 1\n Вы хотите переместить товар? - 2 \n Вы хотите выйти? - 3 \n"))
    except ValueError as err:
        print("Неизвестная команда! Введите число из списка!\n")
    else:
        if a < 1 or a > 3:
            print("Неизвестная команда! Выберите другую!\n")
        if a == 1:
            my_list.append(Off_equip.get_equip(input("Выберите тип техники (p-printer, s-scaner, k-kseroks): ")))
        if a == 2:
            Off_equip.account(my_dict, my_list)
        if a == 3:
            i = 1

