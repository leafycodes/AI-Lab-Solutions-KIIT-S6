# #Create a program that takes user input and checks whether the
# entered number is a prime number or not. Utilize a for loop and
# branching statements.

import math

def isPrime(number):
    if number == 2:
        return True
    for i in range(2, int(math.sqrt(number))): 
        if number % i == 0:
            return False
    return True

number = int(input("enter number: ")) 
if isPrime(number):
    print("prime.")
else:
    print("not prime.")
