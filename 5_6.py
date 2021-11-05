text = open("text_6.txt", "r", encoding="utf-8")

my_dict = {}

for line in text:
    a = line.split()
    count = 0  # переменная для суммы занятий
    for j in range(0, 4):  # обрабатываем полученную строчку-список
        i = ""  # переменная куда складываю отредактированные значения
        for n in a[j]:
            if n == "-":  # пустые значения заменяю нулями для удобства счета
                i = "0"
            else:
                if n == "(":
                    break
                if n == ":":  # убираю двоеточие в названии предмета
                    a[j] = i
                    break
                i = i + n
        if j > 0:  # ставлю условие чтобы не было конфликта типов
            count = count + int(i)
    my_dict.update({a[0]: count})  # собираю словарь

print(my_dict)
text.close()
