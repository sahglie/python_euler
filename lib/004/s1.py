#! /usr/bin/env python

"""A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(a_str):
    return str(a_str) == str(a_str)[::-1]

if __name__ == "__main__":
    print max([x*y for x in range(100, 1000) 
               for y in range(100, 1000) 
               if is_palindrome(x*y)])
