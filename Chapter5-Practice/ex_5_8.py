#以特殊方式和管理员打招呼
names = ['Jack', 'Jobs', 'admin', 'Martin', 'Ava']
for name in names:
    if name == 'admin':
        print("Hello,admin,would you like to see a statues report?")
    else:
        print("Hello " + name + "," + "thank you for logging in again.")

# Hello Jack,thank you for logging in again.
# Hello Jobs,thank you for logging in again.
# Hello,admin,would you like to see a statues report?
# Hello Martin,thank you for logging in again.
# Hello Ava,thank you for logging in again.
