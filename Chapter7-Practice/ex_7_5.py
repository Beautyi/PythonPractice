#电影票
prompt = "\n Tell me your age,I will tell you the price of the ticket."
prompt += "\nEnter 'quit' to end the program."
age = ""

while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        print("Free.")
    elif int(age) < 12:
        print("The price of the ticket is 10.")
    else:
        print("The price of the ticket is 15.")
