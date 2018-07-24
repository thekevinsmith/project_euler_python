# Problem 7 : Statement:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Found 10001st: 104729

def main():
    start = 2
    limit = 200000
    interval = 1
    prime = [1]
    wanted = 10001

    for i in range(start, limit + 1, interval):
        for n in range(start, i, interval):
            if i % n == 0:
                break
        else:
            prime.append(i)
            if len(prime) == wanted:
                print("Found 10001st: %d" % prime[wanted - 1])
    print("Array: %ls" % prime)


if __name__ == '__main__':
    main()