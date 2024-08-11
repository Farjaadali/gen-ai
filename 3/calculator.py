# First Input
num1 = float(input("Enter first number: "))
# 2nd Input
num2 = float(input("Enter second number: "))

# Operator
operation = input("Enter operation (+, -, *, /): ")

if operation == "+" :
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2

# printing output
print(f"Result : {result}")