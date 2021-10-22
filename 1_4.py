n = str(input("Введите число:"))
maxim = 0
for b in n:
    while int(b) > maxim:
        maxim = int(b)

print(maxim)
