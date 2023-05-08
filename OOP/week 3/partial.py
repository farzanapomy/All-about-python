from functools import partial


def ger_number(a, b, c, d):
    return 1000*a + 100*b + 10*c + d


f = partial(ger_number, 1, 2, 3)
print(f(4))
