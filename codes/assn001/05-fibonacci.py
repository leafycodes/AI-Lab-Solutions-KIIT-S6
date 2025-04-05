# Write a Python program to generate the Fibonacci series up to a
# specified number of terms. Use a while loop and branching to
# implement the logic.

a1=0
a2=1
n=int(input("enter number of terms: ")) 

if n==0:
    exit(0)
elif n==1:
    print(a1)
else:
    print(str(a1)+"\n"+str(a2))
    while n-2>0:
        a3=a1+a2
        print(a3)
        a1=a2
        a2=a3
        n-=1
