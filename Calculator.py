def calculate(num1, num2, operator):

    if operator == "+":
        result = num1 + num2
        print(result)

    elif operator == "-":
        result = num1 - num2
        print(result)

    elif operator == "*":
        result = num1 * num2
        print(result)

    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print(result)

    else:
        print("Invalid operator")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

calculate(num1, num2, operator)
