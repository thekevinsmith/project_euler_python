# Problem 3 : Statement:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import sys

def main(k, N):

    if N == 1:
        return

    if N < k:
        return

    if N % k == 0:
        primenumbers.append(k)

        if k != 1:
            return main(k, N / k)
        else:
            return main(k+1, N/k)

    else:
        return main(k+1, N)

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    sys.getrecursionlimit()
    # print(sys.getrecursionlimit())

    primenumbers = []
    largestfactor = 0
    number = 600851475143
    main(1, number)

    for i in primenumbers:
        if i > largestfactor:
            largestfactor = i

    print(primenumbers)
    print(largestfactor)