#!/usr/bin/python3
if (__name__ == '__main__'):
    from calculator_1 import add, sub, div, mul
    import sys
    arguments = len(sys.argv)
    error = "Unknown operator. Available operators: +, -, * and /\n"
    if (arguments != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        fir = int(sys.argv[1])
        operator = str(sys.argv[2])
        sec = int(sys.argv[3])
        if (operator == '+'):
            print('{} {} {} = {}'.format(fir, operator, sec, add(fir, sec)))
        elif (operator == '-'):
            print('{} {} {} = {}'.format(fir, operator, sec, sub(fir, sec)))
        elif (operator == '*'):
            print('{} {} {} = {}'.format(fir, operator, sec, mul(fir, sec)))
        elif (operator == '/'):
            print('{} {} {} = {}'.format(fir, operator, sec, div(fir, sec)))
        else:
            sys.stderr.write(error)
