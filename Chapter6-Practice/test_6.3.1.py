user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
#遍历，key:键，value:值；
for key, value in user_0.items():
    print("\nkey: " + key)
    print("\nvalue: " + value)

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " +
      language.title() +
      ".")
    