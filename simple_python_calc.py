
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply (x,y):
    return x * y
def divide(x,y):
    return x / y


number1 = float(input("Enter first number: "))
operation = input("Choose an operation: ")
number2 = float(input("Enter second number: "))
operation = input("Choose an operation: ")
number3 = float(input("Enter third number: "))
# operation = input("Choose an operation: ")

if operation == '+':
    print(add(number1, number2, number3))
elif operation == '-':
    print(subtract(number1, number2, number3))
elif operation == '*':
    print(multiply(number1, number2, number3))
elif operation == '/':
    print(divide(number1, number2, number3))

