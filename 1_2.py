t = int(input("Введите время в секундах:"))
hour = t // 3600
minut = (t % 3600) // 60
sek = (t % 3600) % 60
print("{:02d}".format(hour), ":", "{:02d}".format(minut), ":", "{:02d}".format(sek))
