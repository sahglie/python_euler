#!/usr/bin/env python

"""There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	n!/r!(n-r)!
It is not until n = 23, that a value exceeds one-million: 23,C,10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are
greater than one-million?
"""

from math import factorial

def choose(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

if __name__ == "__main__":
    over_million = 0
    for n in xrange(100, 0, -1):
        for r in xrange(n, ):
            if choose(n, r) > 1000000: over_million += 1
    print over_million
            

