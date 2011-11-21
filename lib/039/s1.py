#!/usr/bin/env python


"""If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

if __name__ == "__main__":
    maximized_solution = (0, 0)
    for perimeter in xrange(1,  1001):
        solutions = 0
        for a in xrange(1, perimeter):
            for b in xrange(a+1, (perimeter - a)/2):
                c = perimeter - a - b
                if a**2 + b**2 == c**2:
                    solutions += 1
        if solutions > maximized_solution[1]:
            maximized_solution = (perimeter, solutions)
    print maximized_solution
