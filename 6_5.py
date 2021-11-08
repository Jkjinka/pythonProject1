class Stationery:
    title = "Канцелярия"

    def draw(self):
        return print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        return print("Ручка.")


class Pencil(Stationery):
    def draw(self):
        return print("Карандаш.")


class Handle(Stationery):
    def draw(self):
        return print("Маркер.")


a = Stationery()
a.draw()
b = Pen()
b.draw()
c = Pencil()
c.draw()
d = Handle()
d.draw()
