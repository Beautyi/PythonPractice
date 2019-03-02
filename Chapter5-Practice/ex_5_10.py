#检查用户名
current_users = ['Jack', 'Jobs', 'admin', 'Martin', 'Ava']
new_users = [ 'Tom', 'Martin', 'Ava', 'Zoe', 'Rose']
for new_user in new_users:
    if new_user in current_users:
        print("Sorry,you should change the user name.")
    else:
        print("The user name has not be used.")

# The user name has not be used.
# Sorry,you should change the user name.
# Sorry,you should change the user name.
# The user name has not be used.
# The user name has not be used.

current_users = ['Jack', 'Jobs', 'admin', 'Martin', 'Ava']
new_users = [ 'Tom', 'Martin', 'ava', 'Zoe', 'Rose']
for current_user in current_users:
    for new_user in new_users:
        if new_user.lower() in current_user.lower():
            print("Sorry,you should change the user name.")
        else:
            print("The user name has not be used.")
