from art import logo


def add(n1, n2):
    return n1+n2


def substract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = int(input("Enter the First number number?\n"))

    should_continue = True
    while should_continue:
        operation_symbol = input(
            "Pick up any operation from the above:\n+\n-\n*\n/\n")

        num2 = int(input("Enter the second number number?\n"))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start s new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


print(logo)
calculator()
