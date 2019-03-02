#使用多个列表
available_toppings = ['mushrooms', 'green peppers', 'extra cheese','olives', 'pineapple']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry,we do not have " + requested_topping + ".")
    print("\nFinished making your pizza!")
