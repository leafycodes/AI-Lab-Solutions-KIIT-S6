import random

num = random.randint(0, 100)
attempts = 1

print("I have selected a number at random between 0 and 100. Guess it:")

def guessfunc():
    global attempts
    while True:
        userinput = int(input())
        if userinput == num:
            print(f"You won! Attempts taken: {attempts}")
            break
        elif userinput < num:
            print("Too low. Guess higher.")
        else:
            print("Too high. Guess lower.")
        attempts += 1

guessfunc()
