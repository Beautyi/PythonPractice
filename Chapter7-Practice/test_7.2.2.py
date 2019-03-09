#让用户选择何时退出
prompt = "Tell me something,and I will repeat it back to you:"
prompt += "\nEnter  'quit' to end the program. "
message = ""#首次运行while时，message与“quit”比较，但此时用户还没输入，所以先给message赋空值
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
