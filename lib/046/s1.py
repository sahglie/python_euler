#!/usr/bin/env python

"""It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

 9 =  7 + 2 * 1^2
15 =  7 + 2 * 2^2
21 =  3 + 2 * 3^2
25 =  7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

import os, sys
package_root = os.path.abspath(os.path.curdir).split("/")
package_root.pop()
sys.path.insert(0, "/".join(package_root))

from utils import is_prime


def sum_of_prime_and_twice_square(number, primes):
    x = 0
    while primes[x] < number:
        for y in xrange(1, number - primes[x]):
            result = primes[x] + (2 * y**2)
            if number == result: return (primes[x], y)
            elif result > number: break
        x += 1
    return ()


if __name__ == "__main__":
    primes, odd_composites = [], []
    for n in xrange(3, 10000, 2):
        if is_prime(n): primes.append(n)
        else: odd_composites.append(n)

    for c in odd_composites:
        if not sum_of_prime_and_twice_square(c, primes):
            print c
            break
