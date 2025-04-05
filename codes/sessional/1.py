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
