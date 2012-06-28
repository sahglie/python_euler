 #!/usr/bin/env python

"""A Pythagorean triplet is a set of three natural numbers:
a < b < c

for which

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a * b * c.
"""

for a in range(2, 1000):
    for b in range(a+1, 1000):
        if 1000*a + 1000*b - a*b == 500000:
            c = 1000 - a - b
            print (a * b * c)
            break
