n = 1
print("Введите информацию по ПЕРВОМУ товару")
name = input("Введите название товара: ")
price = float(input("Введите цену товара: "))
count = int(input("Введите количество товара: "))
edin = input("Введите единицу измерения: ")
my_dict = {"название": name, "цена": price, "количество": count, "ед": edin}
my_t = (n, my_dict)
my_list = [my_t]
q = input("Хотите ввести новый товар? да или нет: ")
while q == 'да':
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    count = int(input("Введите количество товара: "))
    edin = input("Введите единицу измерения: ")
    my_dict = {"название": name, "цена": price, "количество": count, "ед": edin}
    n = n + 1
    my_t = (n, my_dict)
    my_list.append(my_t)
    q = input("Хотите ввести новый товар? да или нет: ")

print("Полученная структура:")
print(my_list)

print("Аналитический отчет:")
name2 = []
price2 = []  # создаю пустые списки, чтобы в них складывать мнфу из словаря
count2 = []
edin2 = []
for a in my_list:
    name2.append(a[1].get('название'))
    price2.append(a[1].get('цена'))
    count2.append(a[1].get('количество'))
    edin2.append(a[1].get('ед'))

my_dict2 = {"название": set(name2), "цена": set(price2), "количество": set(count2), "ед": set(edin2)}
print(my_dict2)
