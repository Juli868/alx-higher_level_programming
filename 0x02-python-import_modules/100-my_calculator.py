#!/usr/bin/python3
if (__name__ == '__main__'):
    from calculator_1 import add, sub, div, mul
    import sys
    arguments = len(sys.argv)
    if (arguments != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        first = int(sys.argv[1])
        second = int(sys.argv[3])
        operator = sys.argv[2]
        if (operator == '+'):
            print('{} {} {} = {}'.format(first, operator, second, add(first,add)))
        elif(operator == '-'):
            print('{} {} {} = {}'.format(first, operator, second, sub(first,add)))
        elif(operator == '*'):
            print('{} {} {} = {}'.format(first, operator, second, mul(first,add)))
        elif(operator == '/'):
            print('{} {} {} = {}'.format(first, operator, second, div(first,add)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
