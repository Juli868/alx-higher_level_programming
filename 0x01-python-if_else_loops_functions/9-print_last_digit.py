#!/usr/bin/python3
def print_last_digit(number):
    if(type(number) is int or type(number) is float):
        return (number % 10)
