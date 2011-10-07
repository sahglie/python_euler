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
    digits = ['1', '2', '3', '4', '5', '6', '7']
    sol = None
    for n in xrange(9, 0, -1):
        if sol:
            break
        pandigitals = reversed(list(permutations(digits[0:n])))
        for pandigital in pandigitals:
            n = int("".join(pandigital))
            if n % 2 and is_prime(n):
                sol = n
                break
    print sol
