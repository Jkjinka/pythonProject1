import time


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 6:
            t = i % 3
            if t == 0:
                print(self.__color[0])
                time.sleep(7)
            if t == 1:
                print(self.__color[1])
                time.sleep(2)
            if t == 2:
                print(self.__color[2])
                time.sleep(3)
            i = i + 1


a = TrafficLight()
a.running()
