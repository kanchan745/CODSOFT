# Calculator using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("=== Simple Calculator ===")

while True:
    print("\nChoose Operation:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Exit")

    option = input("Enter your choice: ")

    if option == "5":
        print("Calculator Closed.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if option == "1":
        result = add(num1, num2)
    elif option == "2":
        result = subtract(num1, num2)
    elif option == "3":
        result = multiply(num1, num2)
    elif option == "4":
        result = divide(num1, num2)
    else:
        result = "Invalid Option"

    print("Result:", result)
