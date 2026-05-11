# Basic Python calculator

num1 = float(input("enter 1st number: "))
operator = input("enter the operator (+, -, *, /): ")
num2 = float(input("enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator select between (+, -, *, /)")
