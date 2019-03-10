#三个出口，以7_5为例
#1.在while循环中使用条件测试来结束循环


#2.使用变量active来控制循环结束的时机
prompt = "\n Tell me your age,I will tell you the price of the ticket."
prompt += "\nEnter 'quit' to end the program."
age = ""
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    elif int(age) < 3:
        print("Free.")
    elif int(age) < 12:
        print("The price of the ticket is 10.")
    else:
        print("The price of the ticket is 15.")

#3.使用break语句在用户输入‘quit’时退出循环
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
        