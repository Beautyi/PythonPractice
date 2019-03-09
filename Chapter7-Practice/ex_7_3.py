#10的整数倍
number = input("Entre a number, and I will tell you it is a multiple of 10 or not: ")
int_number = int(number)
if int_number % 10 == 0:
    print("\nThe number " + number + " is a multiple of 10." )
else:
    print("\nThe number " + number + " is not a multiple of 10.")
