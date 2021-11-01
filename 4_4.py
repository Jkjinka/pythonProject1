my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print("Начальный список: ", my_list)
new_list = [a for a in my_list if my_list.count(a) == 1]
print("Измененный список: ", new_list)
