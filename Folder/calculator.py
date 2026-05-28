#Annie
#Calculator
#This program prompts users to enter two numbers, an operator, and prints the result of the operation

#Init
#Functions
def main():
    #Welcome Message
    print("Welcome to the simple calculator!")

    #Collect your inputs
    num1 = int(input("Please eneter a number: "))
    num2 = int(input("Please eneter a number: "))
    operator = (input("Please eneter a operation symbol: "))

    #Perform the operation
    if operator == "-":
        print(calc_sub(num1, num2))
    elif operator == "+":
        print(calc_sum(num1, num2))
    elif operator == "*":
        print(calc_mult(num1, num2))
    else:
        print(calc_div(num1, num2))

#This function adds x + y and returns the sum
def calc_sum(x,y):
    return x + y

def calc_sub(x,y):
    return x - y

def calc_mult(x,y):
    return x * y

def calc_div(x,y):
    return x / y

main()
