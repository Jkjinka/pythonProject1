from random import randint

# генерирую файл из 5 чисел
text = open("text_5.txt", "w+", encoding="utf-8")
i = 0
while i < 5:
    text.write(f"{randint(-10000, 10000)} ")
    i = i + 1

# считаю сумму чисел
text.seek(0)
count = 0
for line in text:
    a = line.split()
    for n in a:
        count = count + int(n)

# вывод результатов
text.seek(0)
print(f"Числа в файле: {text.read()}")
print(f"Сумма чисел в файле: {count}")
text.close()
