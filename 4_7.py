def generator(n):
    i = 1
    for el in range(1, n + 1):
        i = i * el
        yield i


n = int(input("Введите факториал до какого числа найти:"))
i = 1
for el in generator(n):
    print(f"{i}!={el}")
    i = i + 1
