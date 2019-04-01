class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("First name is " + self.first_name.title())
        print("Last name is " + self.last_name.title())

    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print('Hello ' + full_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('lili', 'wang')
user1.describe_user()
user1.increment_login_attempts()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
