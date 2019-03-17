#结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the flowing toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(6, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')