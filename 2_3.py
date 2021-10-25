# решение через list
mon = int(input("Введите месяц в виде целого числа: "))  # вводим месяц
time_god = ["Зима", "Весна", "Лето", "Осень"]  # времена года
if mon == 12 or mon < 3:
    print(time_god[0])
if mon > 2 and mon < 6:
    print(time_god[1])
if mon > 5 and mon < 9:
    print(time_god[2])
if mon > 8 and mon < 12:
    print(time_god[3])

# решение через dict
mon = int(input("Введите месяц в виде целого числа: "))  # вводим месяц
time_god2 = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
             10: "Осень", 11: "Осень", 12: "Зима", }
print(time_god2.get(mon))
