#确定列表不是空的
requested_toppings = []
if requested_toppings:#if+列表名用在条件表达式中，至少包含一个元素时返回true,列表为空时返回false
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    