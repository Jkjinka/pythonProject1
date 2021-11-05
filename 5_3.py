text = open("text_3.txt", "r", encoding="utf-8")
# print(f"Количество строк в файле: {len(text.readlines())} ")
# text.seek(0)
print("Сотрудники оклад которых менее 20 тыс:")
i = 0
j = 0
count = 0
for line in text:
    i = i + 1
    a = line.split()
    count = count + float(a[1])
    if float(a[1]) < 20000:
        j = j + 1
        print(f"{j}.{a[0]}")
print("")
print(f"Средний доход сотрудников: {count / i}")
text.close()
