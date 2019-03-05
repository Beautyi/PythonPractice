#将三个字典储存在一个列表中
a = {'first_name': 'da yong', 'last_name': 'sun', 'age': '25', 'city': 'hangzhou'}
b = {'first_name': 'ava', 'last_name': 'rose', 'age': '21', 'city': 'beijing'}
c = {'first_name': 'martin', 'last_name': 'brown', 'age': '30', 'city': 'paris'}
people = [a, b, c]
for person in people:
    print(person)
