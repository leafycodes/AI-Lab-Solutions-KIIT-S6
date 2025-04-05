# Create a Python program that functions as an advanced calculator. It
# should take user input for mathematical expressions and evaluate
# them, supporting basic operations, parentheses, and scientific
# notation.

import math

while True:
    try:
        expression = input("Enter expression: ")
        if expression.lower() == 'exit':
            print("Exiting the calculator.")
            break

        result = eval(expression)
        print(f"Result: {result}\n")
    except Exception as e:
        print("invalid. ")
