class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant's name is " + self.name.title())
        print("Cuisine type is " + self.type.title())

    def open_restaurant(self):
        print('In operation')


my_restaurant1 = Restaurant('金拱门', '快餐')
my_restaurant2 = Restaurant('银拱门', '中餐')
my_restaurant3 = Restaurant('铜拱门', '慢餐')
my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()
