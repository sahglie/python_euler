#!/opt/local/bin/python

"""We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""


DIGITS = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

def extract_digits(n, used):
    while n:
        d = n % 10
        if d in used:
            return False
        used.add(d)
        n /= 10
    return True

def is_pandigital(m1, m2):
    used = set()
    product = m1 * m2
    if not extract_digits(m1, used):
        return False
    if not extract_digits(m2, used):
        return False
    if not extract_digits(product, used):
        return False
    return used == DIGITS


if __name__ == "__main__":
    pandigitals = set()
    for x in xrange(1, 99):
        for y in xrange(x, 9999):
            if is_pandigital(x, y):
                pandigitals.add(x*y)
    print sum(pandigitals)
