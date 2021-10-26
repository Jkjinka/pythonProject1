first_list = list(input("Введите значения списка: "))
print("Мой список:", first_list)
i = 0

while i + 2 <= len(first_list):
    a = first_list[i]
    first_list[i] = first_list[i + 1]
    first_list[i + 1] = a
    i = i + 2
print("")
print("Список после обработки:", first_list)
