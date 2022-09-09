"""
Creation of this app is basically complete. 
There are a lot of more features i can add but not gonna borther with them for now
Thinking to make a actual calculator app using tkinter in future (maybe its already done)
(if it is , its probably gonna be in the same repository as this is in)
"""

import math


class info:
    def __init__(self) -> None:
        pass

    def show():
        print('\n'*100)
        print("""
              █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
              █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄\n""")
        print("""\tWelcome to this dumb calculator app made by an idiot.
        You can do basically anything a normal calculator can do (ok maybe less...)
        Here's the information on what the options mean:
        
        C    => Clear
        +/-  => Change the symbol of current total
        %    => Convert the current total into percentage
        /    => Divide the current total with sum of all the numbers given
        *    => multiplies all the numbers given and the current total
        +    => adds all the numbers given with current total
        -    => subtracts all the numbers given with current total
        ^    => Raises the current total to the power of given number
        =    => Terminates the program
        info => returns back to this screen
        """)
        cont = input("\nPress enter to continue : ")


class calculator:

    def __init__(self) -> None:
        pass

    def show_and_ask(result):
        show_error = False
        while True:
            print("\n"*100)
            print("""
    █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
    █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄\n""")
            print("\t--------------------------")
            print("\t|  C  | +/- |  %  ||  /  |")
            print("\t--------------------------")
            print("\t|  9  |  8  |  7  ||  *  |")
            print("\t|  6  |  5  |  4  ||  +  |")
            print("\t|  3  |  2  |  1  ||  -  |")
            print("\t--------------------------")
            print("\t|  0  |  ^  |info ||  =  |")
            print("\t--------------------------")
            print("\t|{:>23} |".format(result))
            print("\t--------------------------")
            if show_error:
                print("\tPlease Enter a valid operator.")
            operation = input(
                "\n    Enter a valid operator from above : ").lower()

            if operation in ['+', '-', '*', '/', '+/-', 'c', '%', '=', 'info', '^']:
                return operation
            else:
                show_error = True
                continue


class operate:

    def __init__(self, operator, ):
        self.operator = operator

    def calculate(self, total):

        if self.operator == '+':
            while True:
                try:
                    self.numbers = list(
                        map(float, input("    Enter the numbers : ").split()))
                    return total+sum(self.numbers)
                except ValueError:
                    print("    Enter a valid set of numbers.")
                    continue

        elif self.operator == '-':
            while True:
                try:
                    self.numbers = list(
                        map(float, input("    Enter the numbers : ").split()))
                    return total-sum(self.numbers)
                except:
                    print("    Enter a valid set of numbers.")
                    continue

        elif self.operator == '*':
            while True:
                try:
                    self.numbers = list(
                        map(float, input("    Enter the numbers : ").split()))
                    return math.prod(self.numbers)*total
                except:
                    print("    Enter a valid set of numbers.")

        elif self.operator == '/':
            while True:
                try:
                    self.numbers = list(
                        map(float, input("    Enter the numbers : ").split()))
                    return total/sum(self.numbers)
                except:
                    print("    Enter a valid set of numbers.")
                    continue

        elif self.operator == '^':
            while True:
                try:
                    self.numbers = float(
                        input("    Enter one exponential digit."))
                    return total**self.numbers
                except:
                    print("    Enter a valid set of numbers.")
                    continue

        elif self.operator == '+/-':
            return -(total)

        elif self.operator == 'c':
            return 0

        elif self.operator == '%':
            return total/100


total = 0

info.show()

while True:
    operator = calculator.show_and_ask(total)

    if operator == '=':
        print("\n        Your final result is : {}\n".format(total))
        end = input("Press enter to close the terminal.")
        break

    elif operator == 'info':
        info.show()
        continue

    total = operate(operator).calculate(total)
