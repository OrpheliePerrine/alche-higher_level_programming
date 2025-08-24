#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i != 0:
                print(" ", end="")  # add a space between numbers
            print("{:d}".format(num), end="")  # print integer without newline
        print()  # new line after each row

