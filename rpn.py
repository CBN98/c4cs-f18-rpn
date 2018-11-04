#!/usr/bin/env python3
import operator

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
    while True:
        result = calculate(input('rpn calc> '))
        print("Result: ", result)

if __name__ == '__main__':
    main()