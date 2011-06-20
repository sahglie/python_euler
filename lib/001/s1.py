"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_up_to(num):
    multiples = [n for n in range(1, num) if n % 3 == 0 or n % 5 == 0]
    return sum(multiples)


if __name__ == "__main__":
    print sum_up_to(1000)

