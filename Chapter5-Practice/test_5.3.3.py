#if-elif-else语句，,依次检查每个条件测试，直到遇见通过了的条件测试。
age = 2
if age < 4:
    print("Your admission cost is $0!")
elif age < 18:
    print("Your admission cost is $5!")
else:
    print("Your admission cost is $10!")#Your admission cost is $0!

#更简洁的语句
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")#Your admission cost is $5.
