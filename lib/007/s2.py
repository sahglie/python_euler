#!/usr/bin/env python


"""By listing the first six prime numbers:

2, 3, 5, 7, 11, and 13,

we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

from ..utils import sieve_primes

print(sieve_primes(1000000)[10001])