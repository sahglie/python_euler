#!/usr/bin/env python

"""A googol (10^100) is a massive number: one followed by one-hundred zeros;
100*^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
"""

def sum_digits(n):
    total = 0
    while n:
        total += n % 10
        n /= 10
    return total
    
if __name__ == "__main__":
    powers = []
    for a in xrange(1, 100):
        for b in xrange(1, 100):
            powers.append(sum_digits(a**b))
    print max(powers)
