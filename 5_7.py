import json

text = open("text_7.txt", "r", encoding="utf-8")

my_dict = {}
i = 0
avg_count = 0
for line in text:
    a = line.split()
    prib = int(a[2]) - int(a[3])
    if prib > 0:
        i = i + 1
        avg_count = avg_count + prib
    my_dict.update({a[0]: prib})
my_dict_avg = {"Средняя прибыль": (avg_count / i)}

my_list = [my_dict, my_dict_avg]
print(my_list)

with open("my_file_7.json", "w", encoding="utf-8") as write_f:
    json.dump(my_list, write_f)

text.close()
