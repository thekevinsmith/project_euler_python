# Problem 9 : Statement : Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def main():

    # must: a**2 + b**2 = c**2  TRUE
    # and a + b + c = 1000      TRUE
    # find a*b*c = ?            QUESTION
    # #variables and 2 true statements

    # (a**2 + b**2)**(-1) = c
    # 1000 - a - b = c
    # 1000 - a - b = (a**2 + b**2)**(-1)
    # (1000 - a - b)**2 = a**2 + b**2
    # (1000 - a - b)*(1000 - a - b) = a**2 + b**2
    # 1000*1000 -1000a -1000b -1000a +a**2 ab -1000b +ab + b**2 = a**2 + b**2
    # 1 000 000 - 2000a -2000b = 0
    # 500 - a = b -> this is replaced in another formulae

    # TODO:
    # for a
    # for b
    # 1000 - a - b = c
    # if c > 0
    # if c*c = b*b + a*a

    print()


if __name__ == '__main__':
    main()