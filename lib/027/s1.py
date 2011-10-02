#!/opt/local/bin/python

"""Euler published the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n**2  79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n**2 + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""

from math import sqrt

PRIME_CACHE = set()


def is_prime(n):
    if n in PRIME_CACHE: return True
    
    if n < 2: return False
    for i in xrange(2, int(n**.5+1)):
        if not n % i:
            return False
    PRIME_CACHE.add(n)
    return True

def num_primes(a, b):
    n = 0
    primes = 0
    while True:
        if is_prime(n**2 + a*n + b):
            primes += 1
            n += 1
        else:
            return (primes, a, b)


if __name__ == "__main__":
    max = (0, 0, 0)
    for a in xrange(-999, 1000):
        for b in xrange(a, 1000):
            if b % 2 and is_prime(b):
                n = num_primes(a, b)
                if n[0] > max[0]:
                    max = n
    print max[1] * max[2]
            
