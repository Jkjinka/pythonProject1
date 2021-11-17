class Дата:
    def __init__(self, day, mouth, year):
        self.day = day
        self.mouth = mouth
        self.year = year

    @staticmethod
    def valid(obj):
        if obj.day < 1 or obj.day > 31 or obj.mouth < 1 or obj.mouth > 12 or obj.year < 2000:
            print("Дата введена не верно!")
        else:
            print("Дата введена верно!")


    @classmethod
    def get_data(cls, data):
        my_list = data.split("-")
        return cls(int(my_list[0]), int(my_list[1]), int(my_list[2]))


mc = Дата.get_data("19-10-2000")
print(f"{mc.day}-{mc.mouth}-{mc.year}")
Дата.valid(mc)

mc2 = Дата.get_data("19-0-2000")
print(f"{mc2.day}-{mc2.mouth}-{mc2.year}")
Дата.valid(mc2)