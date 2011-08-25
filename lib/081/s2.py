#!/opt/local/bin/python

import sys


if "__main__" == __name__:
    matrix = []
    with open("matrix.txt") as f:
        for line in f.readlines():
            matrix.append(map(int, line.strip().split(",")))

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
            above, left = sys.maxint, sys.maxint

            if not col and not row:
                continue
            if col:
                left = matrix[row][col-1]
            if row:
                above = matrix[row-1][col]
                
            matrix[row][col] += min(above, left)

    print matrix[-1][-1]
