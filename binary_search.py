#!/bin/python3
'''

It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''


def find_smallest_positive(xs):
    if len(xs) == 0:
        return None
    elif xs[-1] <= 0:
        return None

    def go(left, right):
        mid = (left + right) // 2
        if xs[mid] == 0:
            return mid + 1
        if left == right:
            return left
        if xs[mid] < 0:
            left = mid + 1
        if xs[mid] > 0:
            right = mid

        return go(left, right)

    return go(0, len(xs) - 1)


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

    def greater(left, right):
        mid = (left + right) // 2
        if xs[mid] == x:
            if xs[mid - 1] > x:
                return mid - 1
            else:
                right = mid - 1
                return greater(left, right)
        if xs[mid] > x:
            left = mid
            return greater(left, right)

        if xs[mid] < x:
            right = mid
            return greater(left, right)

    def less(left, right):
        mid = (left + right) // 2
        if xs[mid] == x:
            if xs[mid + 1] < x:
                return mid + 1
            else:
                left = mid + 1
                return less(left, right)
        if xs[mid] < x:
            right = mid
            return less(left, right)
        if xs[mid] > x:
            left = mid
            return less(left, right)

    if len(xs) == 0:
        return 0

    if xs[0] == x:
        if xs[-1] == x:
            return len(xs)
        else:
            return less(0, len(xs) - 1)
    elif xs[-1] == x:
        if xs[-2] == x:
            return len(xs) - greater(0, len(xs) - 1) - 1
        else:
            return 1
    if xs[-1] > x:
        return 0

    return less(0, len(xs) - 1) - greater(0, len(xs) - 1) - 1


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
