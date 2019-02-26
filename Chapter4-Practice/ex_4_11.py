pizzas = ['pepperoni', 'mushroom', 'salmon']
friend_pizzas = pizzas[:]
pizzas.append('a')
friend_pizzas.append('b')
print("My favourite pizzas are:")
for pizza in pizzas[0:]:
    print(pizza)

# My favourite pizzas are:
# pepperoni
# mushroom
# salmon
# a

print("My friend favourite pizzas are:")
for pizza in friend_pizzas[0:]:
    print(pizza)

# My friend favourite pizzas are:
# pepperoni
# mushroom
# salmon
# b

