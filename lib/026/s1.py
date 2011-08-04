#! /usr/bin/env python


def calc_cycle_length(num):
    div = 10
    dividends = set([10])
    digits = []

    while div < num:
        digits.append(0)
        div *= 10

    while True:
        if div % num == 0:
            return []

        digit = div / num
        digits.append(digit)
        div = div % num * 10

        if div in dividends:
            return digits
        else:
            dividends.add(div)


if "__main__" == __name__:
    cycles = {}
    for n in range(2, 1000):
        cycle = calc_cycle_length(n)
        if not len(cycle) == 0:
            cycles[len(cycle)] = n

    print cycles[max(cycles.keys())]
