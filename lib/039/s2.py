#!/usr/bin/env python


"""If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

# Based on suggestions by Rayfil
# * Perimeter will always be an even number
# * b = P(P-2a)/2(P-a)


if __name__ == "__main__":
    maximised_solution = (0, 0)
    for P in xrange(2, 1001, 2):
        solutions = 0
        for a in xrange(1, P):
            a = float(a)
            b = (P*(P-2*a)) / (2*(P - a))
            if a >= b: break
            if b.is_integer(): solutions += 1
        if solutions > maximised_solution[1]:
            maximised_solution = (P, solutions)
    print maximised_solution
