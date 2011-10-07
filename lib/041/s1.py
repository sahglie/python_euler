#!/opt/local/bin/python

"""
We shall say that an n-digit number is pandigital if it makes use of
all the digits 1 to n exactly once. For example, 2143 is a 4-digit
pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import os, sys
cmd_folder = os.path.abspath(os.path.curdir).split("/")
cmd_folder.pop()
sys.path.insert(0, "/".join(cmd_folder))
     

from utils import is_prime
from itertools import permutations


if __name__ == "__main__":
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pandigitals = []
    for n in xrange(1, 10):
        pandigitals.extend(permutations(digits[0:n]))
    
    primes = []
    for pandigital in pandigitals:
        n = int("".join(map(str, pandigital)))
        if is_prime(n):
            primes.append(n)
    print max(primes)

