# '''
# 获取用户输入的一个数字，用户输入几就输出一个几层的用‘*’组成的三角形
# 例如 输入3
# 输出
#   *
#  ***
# *****
# '''
# #提示：使用str类的center方法，第一个参数为宽度，第二个为填充的字符
# url = "www.baidu.com"
# print(url.center(40, ' '))
# print(url.center(40, '*'))
# #如上代码输出结果
# #             www.baidu.com
# #*************www.baidu.com**************

usr_input = input("Please input a number: ")
floor_number = int(usr_input)

for i in range(1, floor_number + 1):
    print(((2 * i - 1) * "*").center(2 * floor_number - 1, ' '))
