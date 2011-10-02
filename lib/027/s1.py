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

import itertools
from Queue import PriorityQueue
from math import sqrt


def is_prime(n):
    if n < 2: return False
    for i in xrange(2, int(sqrt(n)+1)):
        if not n % i:
            return False
    return True

def num_primes(a, b):
    n = 0
    primes = 0
    while True:
        if is_prime(n**2 + a*n + b):
            primes += 1
            n += 1
        else:
            return (-1*primes, a, b)


if __name__ == "__main__":
    pq = PriorityQueue()
    for a in xrange(0, 1000):
        for b in xrange(a, 1000):
            pq.put(num_primes(a, b))
            pq.put(num_primes(-1*a, b))
            pq.put(num_primes(a, -1*b))
            pq.put(num_primes(-1*a, -1*b))
    sol = pq.get()
    print sol[1] * sol[2]
            
