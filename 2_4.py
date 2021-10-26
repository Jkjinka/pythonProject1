stroka = input("Введите текст: ")
stroka_list = stroka.split()
n = 0
for a in stroka_list:
    n = n + 1
    print(n, ". ", a[:10])

