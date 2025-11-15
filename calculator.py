print("\t*** Welcome ***")

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))

choice = int(input('''Choices
1. For Addition
2. For Subtraction
3. For Multiplication
4. For Division
Enter your choice: '''))

def Addition(x, y):
    return x + y

def Subtraction(x, y):
    return x - y

def Multiplication(x, y):
    return x * y

def Division(x, y):
    return x / y

if choice == 1:
    print("Result:", Addition(num1, num2))
elif choice == 2:
    print("Result:", Subtraction(num1, num2))
elif choice == 3:
    print("Result:", Multiplication(num1, num2))
elif choice == 4:
    if num2 == 0:
        print("Error: Division by zero is not possible")
    else: 
        print("Result:", Division(num1, num2))
else:
    print("You have entered an invalid choice")
