favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['jen', 'sarah', 'phil', 'ava', 'martin']
names = []

# for name in favourite_languages.keys():
#     names.append(name)

for friend in friends:
    if friend in favourite_languages.keys():
        print(friend.title() + ",thank you for taking our foll.")
    else:
        print(friend.title() + ",please take our foll.")
