#! /usr/bin/env python


def make_change(amount, coins):
    if amount == 0:
        return 1
    elif amount < 0 or len(coins) == 0:
        return 0
    else:
        return make_change(amount - coins[0], coins) + \
               make_change(amount, coins[1:])


if "__main__" == __name__:
    print make_change(200, [200, 100, 50, 20, 10, 5, 2, 1])
