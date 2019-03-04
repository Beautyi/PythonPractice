#遍历字典中的所有键
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favourite_languages.keys():
    print(name.title())
for name in favourite_languages:#省略keys，遍历字典时，会默认遍历所有的键
    print(name.title())
#确定是否接受了调查
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in favourite_languages.keys():
    print("Erin,please take our poll.")
