import random


class Car:

    def __init__(self, r, b, c):
        self.speed = r
        self.color = b
        self.name = c
        self.is_police = False

    def go(self):
        return print(f"На данный момент авто ЕДЕТ!")

    def stop(self):
        return print(f"На данный момент авто ОСТАНАВЛИВАЕТСЯ!")

    def turn(self, direction):
        if direction % 2 == 0:
            return print(f"На данный момент авто повернуло НАЛЕВО!")
        if direction % 2 == 1:
            return print(f"На данный момент авто повернуло НАПРАВО!")

    def show_speed(self):
        return print(f"Скорость - {self.speed} км/ч")

    def traffic(self):  # метод для генерации поездки машины
        b = random.randint(1, 4)
        if b == 1:
            self.go()
        if b == 2:
            self.stop()
        if b == 3 or b == 4:
            self.turn(b)

    def info(self, my_type):  # метод для записи и вывода инфомации машины
        print("")
        print(f"Карточка автомобиля {my_type}:")
        print(f"Тип автомобиля: {my_type}")
        print(f"Наименование - {self.name}")
        print(f"Цвет - {self.color}")
        print(f"Является полицейской - {self.is_police}")
        self.show_speed()


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return print(f"Скорость - {self.speed} км/ч. Вы привысили скорость на {self.speed - 60} км/ч!")
        else:
            return print(f"Скорость - {self.speed} км/ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f"Скорость - {self.speed} км/ч. Вы привысили скорость на {self.speed - 40} км/ч!")
        else:
            return print(f"Скорость - {self.speed} км/ч")


class PoliceCar(Car):

    def __init__(self, r, b, c):
        self.speed = r
        self.color = b
        self.name = c
        self.is_police = True


j = 0
while j < 4:
    speed1 = random.randint(0, 150)
    name1 = input("Введите наименование авто: ")
    color1 = input("Введите цвет авто: ")
    if j == 0:
        a = TownCar(speed1, color1, name1)
        a.info("TownCar")
        a.traffic()
        print("")
    if j == 1:
        a = SportCar(speed1, color1, name1)
        a.info("SportCar")
        a.traffic()
        print("")
    if j == 2:
        a = WorkCar(speed1, color1, name1)
        a.info("WorkCar")
        a.traffic()
        print("")
    if j == 3:
        a = PoliceCar(speed1, color1, name1)
        a.info("PoliceCar")
        a.traffic()
        print("")
    j = j + 1
