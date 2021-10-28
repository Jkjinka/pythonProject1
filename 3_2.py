def func_user(first_name, last_name, years, city, email, phone):
    return "Имя={}, Фамилия={}, год рождения={}, город проживания={}, email={}, телефон={}".format(first_name,
                                                                                                   last_name, years,
                                                                                                   city, email, phone)


print(func_user(first_name="Иван", last_name="Иванов", years=1990, city="Москва", email="123@yandex.ru",
                phone="7-000-000-0000"))
