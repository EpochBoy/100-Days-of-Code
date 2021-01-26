import os
from art import logo

print(logo)

#Calculator

#Addition
def add(n1, n2):
    return n1+n2

#Substraction
def sub(n1, n2):
    return n1-n2

#Multiplication
def multi(n1, n2):
    return n1*n2

#Division
def div(n1, n2):
    return n1/n2

#Operator Dictionary
operations = {
"+":add,
"-":sub,
"*":multi,
"/":div
}

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

#calc runner
state = True

#recursive implementation
def calc():
    num1 = float(input("What's the first number?: "))
    for i in operations:
        print(i)
    user_op = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    result = operations[user_op](num1,num2)
    print(f"{num1}{user_op}{num2} = {result}")

    #enter always once
    while state == True:
        cont = input(f"Want to continue calculating with {result} ? ")
        if cont == "y":
            cls()
            next_op = input("Pick an operation: ")
            next_num = float(input(f"Please input the number you want to {next_op} from {result}: "))
            oldresult = result
            result = operations[next_op](result, next_num)
            print(f"{oldresult}{next_op}{next_num} = {result}")
        else:
            cls()
            print(logo)
            print(f"The final result of your calculation was {result}")
            calc()

calc()