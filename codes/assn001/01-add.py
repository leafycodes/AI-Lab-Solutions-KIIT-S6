# Create a program that takes two numbers as input, adds them, and
# prints the result. Ensure they handle cases where the inputs might be
# strings (requiring type conversion). 

try:
    a = input("first number: ")
    b = input("second number: ")
    
    a = int(a)
    b = int(b)
    
    result = a + b
    
    print(result)
    
except ValueError:
        print("invalid.")

