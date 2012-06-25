#!/usr/bin/env python

"""2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
"""

from ..utils import prime_factors

factors = {}
for x in range(2, 21):
    for (k,v) in prime_factors(x).items():
        factors.setdefault(k, v)
        if k in factors and v > factors[k]:
            factors[k] = v


total = 1
for (k,v) in factors.items():
    total *= k**v
print(total)
