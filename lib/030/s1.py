#!/opt/local/bin/python

"""Surprisingly there are only three numbers that can be written as the
sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""

from itertools import permutations


def sum_of_5th_powers(n):
    total = 0
    while n != 0:
        d = n % 10;
        total += d**5;
        n /= 10;
    return total


if __name__ == "__main__":
    fifth_powers = set()
    for i in xrange(2, 590491):
        if i == sum_of_5th_powers(i):
            fifth_powers.add(i)
    print sum(fifth_powers)
        
