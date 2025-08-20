#!/usr/bin/python3
def print_last_digit(number):
    for n in number:
        n = str(n)[-1]
    print("{}".format(n))
