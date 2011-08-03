#! /usr/bin/env python


def calc_cycle_length(n):
    digits = []
    remainders = set([10])
    d = 10
    
    while True:
        while d < n:
            digits.append(0)
            d *= 10
            
        if (d % n) == 0:
            return []
        else:
            a = d / n
            digits.append(a)
            d = (d - (n * a)) * 10
            if d in remainders:
                return digits
            else:
                remainders.add(d)


if "__main__" == __name__:
    cycles = {}
    for n in range(2, 1000):
        cycle = calc_cycle_length(n)
        if not len(cycle) == 0:
            cycles[len(cycle)] = n

    print cycles[max(cycles.keys())]
