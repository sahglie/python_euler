#!/usr/bin/env python

"""Find the greatest product of five consecutive digits in the 1000-digit number"""

from functools import reduce
import os

file_path = os.path.join(os.path.dirname(__file__), "data.txt")
f = open(file_path)
data = "".join([l.strip() for l in f.readlines()])
f.close()


product = 0
for (i,n) in enumerate(data):
    if len(data[i:i+5]) == 5:
        p = reduce(lambda x,y: int(x)*int(y), list(data[i:i+5]))
        if p > product: product = p

print(product)
