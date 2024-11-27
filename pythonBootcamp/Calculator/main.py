#Calculator
from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    end_of_calculator = False
    while not end_of_calculator:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculator_function = operations[operation_symbol]
        answer = calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit, or type 'r' to start a new calculator.: ").lower()

        if should_continue == 'y':
            num1 = answer
        elif should_continue == 'n':
            end_of_calculator = True
        elif should_continue == 'r':
            end_of_calculator = True
            calculator()

calculator()