def greet_users(names):
    """向列表的每个用户都发出简单的问候"""
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)


usernames = ['hannah', 'tr', 'margot']
greet_users(usernames)
        