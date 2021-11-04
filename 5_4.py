text = open("text_4.txt", "r", encoding="utf-8")
text_new = open("text_4_new.txt", "w", encoding="utf-8")

for line in text:
    a = line.split()
    for n in a:
        if n == 'One':
            n = 'Один'
        if n == 'Two':
            n = 'Два'
        if n == 'Three':
            n = 'Три'
        if n == 'Four':
            n = 'Четыре'
        text_new.write(f"{n} ")
    text_new.write(f"\n")
print("Файл переведен")
text_new.close()
text.close()
