#! /usr/bin/env python

"""A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindromes = set()
for x in range(100, 1000):
    for y in range(x, 1000):
        n = str(x*y)
        if n == n[::-1]: 
            palindromes.add(x*y)
            
print(max(palindromes))
