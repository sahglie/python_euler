#!/usr/bin/env python

from itertools import chain, product, groupby

PANDIGITALS = set('123456789')
def is_pandigital(n):
    digits = str(n)
    return len(digits) == 9 and set(digits) == PANDIGITALS

if __name__ == "__main__":
    pandigitals = []
    nines = [[9], range(90, 100), range(900, 1000), range(9000, 10000)]
    product_pairs = product(chain(*nines), [1, 2, 3, 4, 5])
    for key, group in groupby(product_pairs, lambda x: x[0]):
        group = [str(pair[0]*pair[1]) for pair in group]
        while len(group) > 1:
            pandigital = int("".join(group))
            if is_pandigital(pandigital): pandigitals.append(pandigital)
            group.pop()
    print max(pandigitals)
