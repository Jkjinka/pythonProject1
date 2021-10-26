my_list = [1, 4, 7, 5, 3, 3, 2]
n = int(input("Введите натуральное число: "))  # введенный пользователем элемент
my_list.append(n)  # добавление в список
my_list.sort(reverse=True)  # сортировка
print(my_list)
