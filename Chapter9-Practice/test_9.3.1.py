#继承，子类的方法__int__()
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

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):

    def __init__(self, make, model, year):#类的方法__int__()接受创建Car 实例所需的

        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

