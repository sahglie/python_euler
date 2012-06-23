#! /usr/bin/env python


def make_change(amount, coins, cache = {}):
    """Use memoization for performance
    """
    if amount == 0:
        return 1
    elif amount < 0 or len(coins) == 0:
        return 0
    else:
        key1 = make_key(amount - coins[0], coins)
        key2 = make_key(amount, coins[1:])

        if cache.has_key(key1):
            val1 = cache[key1]
        else:
            val1 = make_change(amount - coins[0], coins, cache)
            cache[key1] = val1

        if cache.has_key(key2):
            val2 = cache[key2]
        else:
            val2 = make_change(amount, coins[1:], cache)
            cache[key2] = val2

        return val1 + val2

def make_key(amount, coins):
    return "%s - %s" %(amount, len(coins))


if "__main__" == __name__:
    print make_change(200, [200, 100, 50, 20, 10, 5, 2, 1])
