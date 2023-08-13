#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    print_matrix_integer = __import__('1-print_matrix_integer').print_matrix_integer
    for row in matrix:
        for i in range(len(row)):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(row[i]), end="")
        print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print_matrix_integer(matrix)






