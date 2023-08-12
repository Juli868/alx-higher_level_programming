#!/usr/bin/python3
if (__name__ == '__main__'):
    from calculator_1 import add, sub, div, mul
    import sys
    arguments = len(sys.argv)
    if (arguments != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        fir = int(sys.argv[1])
        sec = int(sys.argv[3])
        operator = sys.argv[2]
        if (operator == '+'):
            print('{} {} {} = {}'.format(fir, operator, sec, add(fir, sec)))
        elif(operator == '-'):
            print('{} {} {} = {}'.format(fir, operator, sec, sub(fir, sec)))
        elif(operator == "*"):
            print('{} {} {} = {}'.format(fir, operator, sec, mul(fir, sec)))
        elif(operator == '/'):
            print('{} {} {} = {}'.format(fir, operator, sec, div(fir, sec)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
