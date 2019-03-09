#求模运算符，%返回余数
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)

#求一个数是奇数还是偶数
number = input("Entre a number, and I will tell you it is even or odd: ")
int_number = int(number)
if int_number % 2 == 0:
    print("\nThe number " + number + " is even." )
else:
    print("\nThe number " + number + " is odd.")
