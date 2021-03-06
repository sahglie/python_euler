#!/usr/bin/env python

"""By replacing the 1st digit of *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

import os, sys
package_root = os.path.abspath(os.path.curdir).split("/")
package_root.pop()
sys.path.insert(0, "/".join(package_root))

from utils import is_prime


def is_prime_family(masks, size):
    db = dict().fromkeys(masks, 0)
    for key,val in db.items():
        for n in range(0, 10):
            if n == 0 and key[0] == "*": continue
            num = int(key.replace("*", str(n)))
            if is_prime(num): db[key] += 1
        if db[key] == size:
            return True
    return False


if __name__ == "__main__":
    digits = "0123456789"
    prime = 56003
    while True:
        if is_prime(prime):
            p = str(prime)
            masks = [p.replace(d, "*") for d in digits if p.count(d) > 1]
            if is_prime_family(masks, 8): break
        prime += 2
    print prime
