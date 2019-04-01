#通过方法对属性的值进行递增
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + " " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        self.odometer_reading += miles


my_used_car = Car('bmw', 'X5', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23900)
my_used_car.read_odometer()
my_used_car.increment_odometer(900)
my_used_car.read_odometer()
