# '''
# 用dict实现一个数据库，实现增删改查功能。
# 可以按空格拆分用户输入，再根据指令的数量和内容进行具体操作
# 例：
# 增：
# 输出：please input command：
# 输入：add tony 123456 beijing
# 删：
# 输出：please input command：
# 输入：del tony
# 输出：del tony ok
#
# 改：
# 输出：please input command：
# 输入：update tony tel-number 555555
# 输出：update tony tel-number ok
#
# 输出：please input command：
# 输入：query tony
# 输出：
# tel-number：123456
# address：beijing
# 输入：query tony address
# beijing
#
# '''

dic = {}
name = input("please tell me your name")
tel_number = input("please tell me your tel_number")
address = input("please tell me your address")
dic["name"] = name
dic["tel_number"] = tel_number
dic["address"] = address
print(dic)

message = input("Please tell me what do you want to delete?")
del dic[str(message)]
print(dic)

message_02 = input("Please tell me what do you want to replace?")
message_03 = input("What do you want to replace it with?")
dic[str(message_02)] = message_03
print(dic)

while True:
    message_04 = input("Please tell me what do you want to find?And input 'quit' to end the program.")
    if str(message_04) == 'quit':
        break
    elif str(message_04) == 'name':
        print(dic['name'])
    elif str(message_04) == 'tel_number':
        print(dic['tel_number'])
    else:
        print(dic['address'])
