# Write a program that calculates the area of a rectangle using user-
# input length and width, and then compare it with the area of a
# square with side length half of the rectangle's width.

l=int(input("length: "))
w=int(input("width: "))
 
s=w/2
print("area of rectangle "+str(w*l)+" sq, area of square "+str(s*s)+" sq")

print("area of rectangle is "+str(w*l-s*s)+" larger than area of square ")