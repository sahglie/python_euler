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

import os, sys
cmd_folder = os.path.abspath(os.path.curdir).split("/")
cmd_folder.pop()
sys.path.insert(0, "/".join(cmd_folder))

from utils import is_pandigital

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    pandigitals = []
    while len(numbers) > 1:
        for i in [9, 99, 999, 9999]:
            pandigital = "".join([str(i * n) for n in numbers])
            if len(pandigital) > 9:
                break
            elif is_pandigital(int(pandigital)):
                pandigitals.append(int(pandigital))
        numbers.pop()
    print max(pandigitals)
