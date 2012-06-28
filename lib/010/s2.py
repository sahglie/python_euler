#!/usr/bin/env python

"""Find the sum of all the primes below two million"""

from ..utils import sieve_primes

print(sum(sieve_primes(2000000)))
