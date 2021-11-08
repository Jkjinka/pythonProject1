class Worker:

    def __init__(self, a, b):
        self.name = a  # 'Иван'
        self.surname = b  # 'Иванов'
        self.position = 'Менеджер'
        self._income = {"оклад": 1000, "премия": 500}


class Position(Worker):

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return print(f"Полное имя сотрудника: {full_name}")

    def get_total_income(self):
        total_income = self._income.setdefault("оклад") + self._income.setdefault("премия")
        return print(f"Доход сотрудника: {total_income} рублей")


print("Введите данные работника: ")
a = input("Введите имя: ")
b = input("Введите фамилию: ")
d = Position(a, b)
print("")
print("Карточка сотрудника: ")
d.get_full_name()
print(f"Должность: {d.position}")
d.get_total_income()
