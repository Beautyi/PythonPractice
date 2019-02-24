'''
获取用户输入的字符串然后按如下形式输出。用list实现。
+------------+
|            |
| User input |
|            |
+------------+
'''

user_input = input("Please input some words:\n")
input_len = len(user_input)

first = "+" + input_len * "-" + "+"
second = "|" + input_len * " " + "|"
usr_input = "|" + user_input + "|"

print(first)
print(second)
print(usr_input)
print(second)
print(first)

'''
Please input some words:
bigbigbig
+---------+
|         |
|bigbigbig|
|         |
+---------+
'''
