class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant's name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())
        print(str(self.number_served) + " people have had dinner here.")

    def open_restaurant(self):
        print('In operation')

    def set_number_served(self, people):
        self.number_served = people

    def increment_number_served(self, people):
        self.number_served += people


restaurant = Restaurant('金拱门', '快餐')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(10)
restaurant.describe_restaurant()
restaurant.increment_number_served(3)
restaurant.describe_restaurant()
