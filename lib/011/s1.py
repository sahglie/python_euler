#! /usr/bin/env python


def load_matrix(file="data.txt"):
    fd = open(file)
    matrix = []
    for line in fd.readlines():
        matrix.append([int(elem) for elem in line.split()])
    fd.close()
    return matrix

def mult(x, y):
    return x * y

def max_in_4x4(row, col, matrix):
    row_prod1 = reduce(mult, [matrix[row][c] for c in range(col, col+4)])
    row_prod2 = reduce(mult, [matrix[row+3][c] for c in range(col, col+4)])
    col_prod1 = reduce(mult, [matrix[r][col] for r in range(row, row+3)])
    col_prod2 = reduce(mult, [matrix[r][col+3] for r in range(row, row+3)])
    diag_prod1 = matrix[row][col] * matrix[row+1][col+1] * matrix[row+2][col+2] * matrix[row+3][col+3]
    diag_prod2 =  matrix[row+3][col] * matrix[row+2][col+1] * matrix[row+1][col+2] * matrix[row][col+3]
    return max(row_prod1, row_prod2, col_prod1, col_prod2, diag_prod1, diag_prod2)
    
def find_max_product(matrix):
    products = [max_in_4x4(row, col, matrix)
                for row in range(0, 16)
                for col in range(0, 16)]
    return max(products)

    
if "__main__" == __name__:
    print find_max_product(load_matrix())
