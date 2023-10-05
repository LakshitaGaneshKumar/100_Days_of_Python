from calculator_art import logo


#calculator functions
#add
def add(x, y):
    return x + y


#subtract
def subtract(x, y):
    return x - y


#multiply
def multiply(x, y):
    return x * y


#divide
def divide(x, y):
    return x / y


#dictionary of operations
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    continue_calc = "y"
    num1 = float(input("What's the first number?: "))

    #loop through operations and print them out for the user to choose
    for sign in operations:
        print(sign)

    while continue_calc == "y":
        #generate user input
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))

        #compute
        answer = operations[operation_symbol](num1, num2)

        #print result
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        #determine if user wants to continue
        continue_calc = input(
            f"Type 'y' to continue calculation with {answer}, type 's' to start over, or 'n' to exit: "
        )
        if continue_calc == "y":
            num1 = answer
        elif continue_calc == "s":
            calculator()


print(logo)
calculator()
print()
print("Thanks for using the Calculator!")
