def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the flowing toppings:")
    for topping in toppings:
        print("- " + topping)
