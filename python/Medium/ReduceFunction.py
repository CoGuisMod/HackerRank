from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator


fracs = [Fraction(1, 2), Fraction(3, 4), Fraction(10, 6)]
print(product(fracs))
