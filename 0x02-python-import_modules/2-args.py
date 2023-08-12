#!/usr/bin/python3
if (__name__ == '__main__'):
    import sys
    counter = len(sys.argv)
    if (counter == 1):
        print("0 arguments.")
    elif (counter == 2):
        print("{} argument".format(counter -1))
    else:
        print("{} arguments:".format(counter -1))
    for count in range(1, counter):
        print("{}: {}".format((count), sys.argv[count]))
