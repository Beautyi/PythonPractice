#城市
cities = {
    'paris': {
        'country': 'france',
        'population': '110 million',
        'landmark': 'eiffel tower',
    },
    'beijing': {
        'country': 'china',
        'population': '300 million',
        'landmark': 'the palace museum',
    },
}
for city, information in cities.items():
    country = information['country']
    population = information['population']
    landmark = information['landmark']
    print("\n" + country.title() + " has " + population + "people,and it's landmark is " + landmark.title() + ".")
