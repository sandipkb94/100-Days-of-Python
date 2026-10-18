def add(x,y) :
    return x + y

def subtract(x,y) :
    return x - y

def multiply(x,y) :
    return x * y

def divide(x,y) :
    return x / y
#add these functions into a dictionary as the values. keys = "+","-","*","/"
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# Use dictionary operations to perform the calculation
def calculator():
    should_accumulate = True
    number1 = float(input("What is the first numner?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        number2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](number1,number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")

        choice = input(f"Type y to continue calculation with {answer} and type n to start a new calculation. ")

        if (choice == "y") or (choice == "Y") :
             number1 = answer
        else: 
            should_accumulate = False
            print("\n" * 2)
            calculator()

calculator()