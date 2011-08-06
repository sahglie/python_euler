#!/opt/local/bin/python


import math

"""A Pythagorean triplet is a set of three natural numbers:
a < b < c

for which

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a * b * c.
"""


def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2 and a < b and b < c
    

def find_pythagorean_triplet():
    for a in range(1, 999):
        for b in range(1, 999):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == 1000 and is_pythagorean_triplet(a, b, c):
                return (a, b, c)


if "__main__" == __name__:
    print reduce(lambda x,y: x*y, find_pythagorean_triplet())
        
