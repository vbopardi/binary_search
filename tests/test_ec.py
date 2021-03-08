from binary_search import argmin_simple, find_boundaries


def test__find_boundaries_1():
    x_min = 0
    f = lambda x: (x-x_min)**2
    lo,hi = find_boundaries(f)
    assert lo <= x_min <= hi

def test__find_boundaries_2():
    x_min = 10
    f = lambda x: (x-x_min)**2
    lo,hi = find_boundaries(f)
    assert lo <= x_min <= hi

def test__find_boundaries_3():
    x_min = -10
    f = lambda x: (x-x_min)**2
    lo,hi = find_boundaries(f)
    assert lo <= x_min <= hi

def test__find_boundaries_4():
    x_min = 1e10
    f = lambda x: (x-x_min)**2
    lo,hi = find_boundaries(f)
    assert lo <= x_min <= hi

def test__find_boundaries_5():
    x_min = -1e10
    f = lambda x: (x-x_min)**2
    lo,hi = find_boundaries(f)
    assert lo <= x_min <= hi

def test__argmin_1():
    epsilon = 1e-3
    x_min = 0
    f = lambda x: (x-x_min)**2
    assert abs(argmin_simple(f,epsilon)-x_min) <= epsilon

def test__argmin_2():
    epsilon = 1e-3
    x_min = 10
    f = lambda x: (x-x_min)**2
    assert abs(argmin_simple(f,epsilon)-x_min) <= epsilon

def test__argmin_3():
    epsilon = 1e-3
    x_min = -10
    f = lambda x: (x-x_min)**2
    assert abs(argmin_simple(f,epsilon)-x_min) <= epsilon

def test__argmin_3():
    epsilon = 1e-3
    x_min = -1e10
    f = lambda x: (x-x_min)**2
    assert abs(argmin_simple(f,epsilon)-x_min) <= epsilon

def test__argmin_3():
    epsilon = 1e-3
    x_min = 1e10
    f = lambda x: (x-x_min)**2
    assert abs(argmin_simple(f,epsilon)-x_min) <= epsilon
