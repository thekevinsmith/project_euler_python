# Problem 6: Statement:
# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + .... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 55**2 = 3025
# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


def main():
    start = 1
    limit = 100
    interval = 1
    squareSum = 0
    sumSquares = 0

    for i in range(start, (limit + 1), interval):
        sumSquares = sumSquares + i**2
        squareSum += i
    squareSum = squareSum**2

    differenceRes = squareSum - sumSquares
    print(sumSquares)
    print(squareSum)
    print("squareSum - sumSquares = %d" % differenceRes)


if __name__ == '__main__':
    main()