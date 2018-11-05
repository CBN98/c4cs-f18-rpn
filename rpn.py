#!/usr/bin/env python3
import operator
from colorama import init, deinit, Fore, Back

op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '^': operator.pow
}

def calculate(arg):
    #stack for calculator
    stack = list()

    #process tokens
    for token in arg.split():
        if token == 'q':
            quit()
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()

            #Look up function in table
            func = op[token]
            result = func(val1, val2)

            stack.append(result)

    return stack.pop()

def main():
    init()
    print(Fore.BLUE + Back.YELLOW + 'RPN CALCULATOR')
    while True:
        print(Fore.BLUE + Back.YELLOW)
        result = calculate(input('rpn calc> '))
        print(Fore.RED + Back.WHITE + "Result: ", result)

if __name__ == '__main__':
    main()
    deinit()