text = open("1_text.txt", "r", encoding="utf-8")
print(f"Количество строк в файле: {len(text.readlines())} ")
text.seek(0)
i = 1
for line in text:
    a = line.split()
    print(f"Количество слов в {i} строке: {len(a)}")
    i = i + 1

text.close()
