#编写清晰的程序
name = input("Please enter your name: ")
print("Hello, " + name.title() + "!")

#有时候提示可能会超过一行，这时需要把提示存储在一个变量中，再将该变量传递给函数input（）。
prompt = "If you tell us who you are,we can personalize the messages you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("Hello, " + name.title() + "!")
