def city_country(city, country):
    name = city.title() + " ," + country.title()
    return name


name_1 = city_country("beijing", "china")
print(name_1)
name_2 = city_country("hangzhou", "china")
print(name_2)
name_3 = city_country("washington", "america")
print(name_3)
