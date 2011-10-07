#!/opt/local/bin/python

"""
We shall say that an n-digit number is pandigital if it makes use of
all the digits 1 to n exactly once. For example, 2143 is a 4-digit
pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""


"""
Math tip: one can determine if N is divisible by X by summing
the digits of N and then dividing by X.  If the digit sum of N
is evenly divisible by X then X divides N

So in this problem, we know that any pandigital of length 8 or 9
is not prime:
1 + ... + 9 % 3 == 0
1 + ... + 8 % 3 == 0
"""

import os, sys
cmd_folder = os.path.abspath(os.path.curdir).split("/")
cmd_folder.pop()
sys.path.insert(0, "/".join(cmd_folder))
     

from utils import is_prime
from itertools import permutations


if __name__ == "__main__":
    digits = ['1', '2', '3', '4', '5', '6', '7']
    primes = []
    for n in xrange(1, 10):
        for pandigital in permutations(digits[0:n]):
            n = int("".join(pandigital))
            if n % 2 and is_prime(n):
                primes.append(n)
    print max(primes)

