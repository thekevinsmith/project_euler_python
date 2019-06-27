# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?




def main():
    print()

    res = str(2**1000)
    final = 0

    for d in range(len(res)):
        final += int(res[d])

    print(final)  # answer: 1366


if __name__ == '__main__':
    main()