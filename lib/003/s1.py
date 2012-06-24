#!/usr/bin/env python

"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29. What is the 
largest prime factor of the number 600_851_475_143
"""

d, n = 2, 600851475143
while n > 1:
    if n % d == 0: n /= d
    else: d += 1

print(d)
