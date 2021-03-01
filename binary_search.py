#!/bin/python3
'''

It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''


def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT:
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    if len(xs) == 0:
        return None
    elif len(xs) == 1:
        if xs[0] > 0:
            return 0
        else:
            return None
    else:
        if min(xs) > 0:
            return 0
        elif max(xs) <= 0:
            return None
        else:
            neg = [num for num in xs if num <= 0]
            return len(neg)


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT:
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''

    xlist = [num for num in xs if num == x]

    return len(xlist)


def argmin(f, lo, hi, epsilon=1e-3):
    if hi - lo < epsilon:
        return hi
    else:
        p1 = lo + (hi - lo) / 3
        p2 = lo + (hi - lo) / 3 * 2

        xs = [lo, p1, p2, hi]
        evallist = [f(x) for x in xs]

        mydict = {k: v for (k, v) in zip(xs, evallist)}
        sortdict = sorted(mydict.items(), key=lambda kv: kv[1])

        if sortdict[0][0] > sortdict[1][0]:
            return argmin(f, sortdict[1][0], sortdict[0][0], epsilon)
        else:
            return argmin(f, sortdict[0][0], sortdict[1][0], epsilon)
