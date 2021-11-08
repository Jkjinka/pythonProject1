class Road:
    m_one = 25  # буду считать что это 2 гостовых значения в этом регионе
    hight_stand = 5

    def __init__(self, a, b):
        self._length = a
        self._width = b

    def massa(self):
        m = self._length * self._width * self.m_one * self.hight_stand
        return print(f"Для покрытия дороги {self._length}м х {self._width}м необходимо {m} кг асфальта")


d = Road(float(input("Введите длину дороги в метрах: ")), float(input("Введите ширину дороги в метрах: ")))
d.massa()
