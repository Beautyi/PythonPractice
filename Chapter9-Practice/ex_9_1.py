class Restaurant:

    def _init_(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant's name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print('In operation')

    my_restaurant = Restaurant('金拱门','快餐')
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
