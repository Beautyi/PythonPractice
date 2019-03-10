#三个出口
#电影票
prompt = "\n Tell me your age,I will tell you the price of the ticket."
prompt += "\nEnter 'quit' to end the program."
age = ""

while 'quit' !=  input(prompt):
    int_age = int(age)
    if int_age < 3:
        print("Free.")
    elif int_age < 12:
        print("The price of the ticket is 10.")
    else:
        print("The price of the ticket is 15.")
