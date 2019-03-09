#使用break退出循环
prompt = "Tell me something,and I will repeat it back to you:"
prompt += "\nEnter  'quit' to end the program. "
while True:
    city = input(prompt)
    if city == 'quit':
        break
