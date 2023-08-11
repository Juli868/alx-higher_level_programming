#!/usr/bin/python3
if (__name__ == '__main__'):
    import sys
    sum = 0
    counter = len(sys.argv)
    if (counter > 1):
        for count in range(1, counter):
            sum += int(sys.argv[count])
    print(sum)
