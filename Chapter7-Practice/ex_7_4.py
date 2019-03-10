#披萨配料
prompt = "\nPlease input the ingredient:"
prompt += "\nEnter 'quit' to end the program."
ingredients = ""
while ingredients != 'quit':
    ingredients = input(prompt)#input后进入循环，否则会出现无限循环的情况。
    if ingredients != 'quit':
        print("We will mix the " + ingredients + " to the pizza.")
