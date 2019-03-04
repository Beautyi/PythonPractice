#遍历字典中的所有值，不是键
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())#由重复项

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):#用set找出列表中独一无二的元素
    print(language.title())
    