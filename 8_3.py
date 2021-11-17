class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


i = 0
my_list = []
while i == 0:
    n = input("Введите данные: ")
    if n == "stop":
        i = 1
        break
    try:
        if not n.isdigit():
            raise ZeroError("Введите число!")
    except ZeroError as err:
        print(err)
    else:
        my_list.append(int(n))

print(my_list)
