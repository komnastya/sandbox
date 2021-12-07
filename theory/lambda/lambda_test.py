# TESTING LAMBDAS

# Python lambdas can be tested similarly to regular functions.

l_func = lambda x: (x + 2) * 5

def test_l_func_natural_number():
    assert l_func(3) == 25
    assert l_func(8) == 50

def test_l_func_negative_number():
    assert l_func(-2) == 0
    assert l_func(-13) == -55

def test_l_funct_rational_number():
    assert l_func(0.5) == 12.5
    assert l_func(-3.5) == -7.5
