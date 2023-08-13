#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple
    new_matrix = []
    for row in matrix:
        new_row = [value**2 for value in row]
        new_matrix.append(new_row)
    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_matrix = square_matrix_simple(matrix)
for row in result_matrix:
    print(row, end="")