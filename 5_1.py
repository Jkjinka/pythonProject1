text = open("1_text.txt", "w", encoding="utf-8")
a = input("Введите текст для записи в файл: ")
while a != "":
    text.write(f"{a}\n")
    a = input()

text.close()
