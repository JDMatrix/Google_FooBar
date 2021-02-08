from decimal import Decimal, getcontext
from fractions import Fraction


def solution(n):
    sqr_of_2 = Fraction(Decimal(2).sqrt())
    total = recursion(sqr_of_2, Fraction(n))
    return str(int(total))


def recursion(sqr_of_2, number):
    if number > 0:
        getcontext().prec = 101

        # Important to use int() here instead of Math.floor()
        number_prime = Fraction(int((sqr_of_2 - Fraction(1)) * Fraction(number)))

        return number * number_prime + ((number * (number + Fraction(1))) / Fraction(2)) - (
                (number_prime * (number_prime + Fraction(1))) / Fraction(2)) - recursion(sqr_of_2, number_prime)

    return Fraction(0)


def main():
    assert solution('5') == '19'
    assert solution('77') == '4208'
    assert solution('10000') == '70712749'
    assert solution(10**100) == \
           '70710678118654752440084436210484903928483593768847403658833986899536623923105351942519376716382078638821760123411090095254685423841027253480565451739737157454059823250037671948325191776995310741236436'


if __name__ == '__main__':
    main()
