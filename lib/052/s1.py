#!/usr/bin/env python


"""It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

def same_digits_upto_factor(number, factor):
    if factor == 0: return True
    else:
        return digits(number) == digits(factor*number) and \
               same_digits_upto_factor(number, factor-1)
    
def digits(n):
    digits = []
    while n:
        digits.append(n % 10)
        n /= 10
    digits.sort()
    return digits
    

if __name__ == "__main__":
    for i in xrange(3, 1000000):
        if same_digits_upto_factor(i, 6): break
    print i
