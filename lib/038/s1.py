#!/usr/bin/env python

"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

import itertools

PANDIGITAL = set('123456789')
def is_pandigital(number):
    digits = str(number)
    return len(digits) == 9 and set(digits) == PANDIGITAL

if __name__ == "__main__":
    pandigitals = []
    numbers = [1, 2, 3, 4, 5]
    nines = [[9], range(90, 100), range(900, 1000), range(9000, 10000)]
    for i in itertools.chain(*nines):
        pandigital = "".join([str(i * n) for n in numbers])
        if len(pandigital) > 9:
            numbers.pop()
        elif is_pandigital(int(pandigital)):
            pandigitals.append(int(pandigital))
    print max(pandigitals)
