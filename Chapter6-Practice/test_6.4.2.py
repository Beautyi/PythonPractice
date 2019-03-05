#在字典中存储列表
#字典中将一个键关联多个值时，可以在字典中嵌套一个列表
favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']

    }
for name, languages in favourite_languages.items():
    print("\n" + name.title() + "'sfavourte languages are:")
    for language in languages:
        print("\t" + language.title())
