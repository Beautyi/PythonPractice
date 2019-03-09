#使用标志
#在要求很多条件都满足才运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态，这个变量被称为标志。
prompt = "Tell me something,and I will repeat it back to you:"
prompt += "\nEnter  'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message != 'quit':
        active = False
    else:
        print(message)
