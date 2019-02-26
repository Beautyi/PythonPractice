my_foods = ['pizza', 'carrot', 'cake']
friend_foods = my_foods[:]#复制列表
print("My favourite foods are: ")
print(my_foods)
print("My friend favourite foods are: ")
print(friend_foods)

# My favourite foods are:
# ['pizza', 'carrot', 'cake']
# My friend favourite foods are:
# ['pizza', 'carrot', 'cake']

my_foods = ['pizza', 'carrot', 'cake']
friend_foods = my_foods[:]#使用复制列表,各自新增后，对方不新增，不是简单的等于
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favourite foods are: ")
print(my_foods)
print("My friend favourite foods are: ")
print(friend_foods)

# My favourite foods are:
# ['pizza', 'carrot', 'cake', 'cannoli']
# My friend favourite foods are:
# ['pizza', 'carrot', 'cake', 'ice cream']

my_foods = ['pizza', 'carrot', 'cake']
friend_foods = my_foods#简单的等于，一方增加全增加
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favourite foods are: ")
print(my_foods)
print("My friend favourite foods are: ")
print(friend_foods)

# My favourite foods are:
# ['pizza', 'carrot', 'cake', 'cannoli', 'ice cream']
# My friend favourite foods are:
# ['pizza', 'carrot', 'cake', 'cannoli', 'ice cream']

