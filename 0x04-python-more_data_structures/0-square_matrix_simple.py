#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda m: list(map(lambda y: y**2, m)), matrix))
