class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("First name is " + self.first_name.title())
        print("Last name is " + self.last_name.title())

    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print('Hello ' + full_name.title())


user1 = User('lili', 'wang')
user2 = User('shuai', 'sun')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()


