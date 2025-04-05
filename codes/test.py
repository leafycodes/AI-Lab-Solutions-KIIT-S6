def cool_func():
    a=int(input("Enter number:"))
    b=int(input("Enter 2nd number:"))
    return a+b

print("hi guys")
print(type(cool_func()))

a=100
b="Hello Anish"
c=b
print(id(a))
print(id(b))
print(id(c))
a=40
print(id(a))

print("The type of a", type(a))

b = 40.5
print(" b is a float number", isinstance(40.5,float))

print("The type of b", type(b))

c = 1+3j

print("The type of c", type(c))

print(" c is a complex number", isinstance(1+3j,complex))

str1 = 'welcome to KIIT' #string str1

str2 = ' how are you' #string str2

print (str1[0:2]) #printing first two character using slice operator

print (str1[4]) #printing 4th character of the string

print (str1*2) #printing the string twice

print (str1 + str2) #printing the concatenation of str1 and str2

list1 = [1, "hi", "Python", 2]

#Checking type of given list

print(type(list1))

#Printing the list1

print (list1)

# List slicing

print (list1[3:])

# List slicing

print (list1[0:2])

# List Concatenation using + operator

print (list1 + list1)

# List repetation using * operator

print (list1 * 3)

d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}

# Printing dictionary

print (d)

# Accesing value using keys

print("1st name is "+d[1])

print("2nd name is "+ d[4])

print (d.keys())

print (d.values())

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a>b and a>c:
    print("a is largest")
if b>a and b>c:
    print("b is largest")
if c>a and c>b:
    print("c is largest")

#Creating a sequence which is a tuple of numbers

numbers = (4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2)
# variable to store the square of the number
square = 0
# Creating an empty list
squares = []
# Creating a for loop
for value in numbers:
    square = value ** 2
    squares.append(square)

print("The list of squares is", squares)

string = "Python Loop"
# Initiating a loop
for s in string:
# giving a condition in if block
    if s == "o":
        print("If block")
# if condition is not satisfied then else block will be execute
    else:
        print(s)

