prime_list = []
number = 0
isPrime = True

for number in range(2, 100):
    isPrime = True
    
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break

    if isPrime == True:
        prime_list.append(number)

print(prime_list) 
