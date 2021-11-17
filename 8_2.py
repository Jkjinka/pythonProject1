class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


count = input("Введите дробь, через /: ")
my_list = count.split("/")

try:
    if int(my_list[1]) == 0:
        #print("2")
        raise ZeroError("Делить на ноль нельзя!")

except ZeroError as err:
    print(err)

else:
    print(f"Результат: {count}={int(my_list[0])/int(my_list[1])}")
