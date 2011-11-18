#!/usr/bin/env python

import os, sys
cmd_folder = os.path.abspath(os.path.curdir).split("/")
cmd_folder.pop()
sys.path.insert(0, "/".join(cmd_folder))

import itertools

PANDIGITALS = set('123456789')
def is_pandigital(n):
    digits = str(n)
    return len(digits) == 9 and set(digits) == PANDIGITALS

if __name__ == "__main__":
    pandigitals = []
    product_pairs = itertools.product([9, 99, 999, 9999], [1, 2, 3, 4, 5])
    for key, group in itertools.groupby(product_pairs, lambda x: x[0]):
        product = int("".join([str(pair[0]*pair[1]) for pair in group]))
        if is_pandigital(product): pandigitals.append(product)
    print max(pandigitals)
