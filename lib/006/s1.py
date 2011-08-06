#!/opt/local/bin/python

"""The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""

def square_of_sums(n):
    return (n*(n+1)/2)**2

def sum_of_squares(n):
    return n*(n+1)*(2*n+1)/6


if "__main__" == __name__:
    print square_of_sums(100) - sum_of_squares(100)
