# Problem 10 : Statement : Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def main():
    start = 2
    limit = 2000000
    interval = 1
    #prime = [1] #if we dont exclude 1
    prime = []
    mysum = 0

    for i in range(start, limit + 1, interval):
        for n in range(start, i, interval):
            if i % n == 0:
                break
        else:
            prime.append(i)
            print(i)
    for i in prime:
        mysum += prime[i]
    print(mysum)


if __name__ == '__main__':
    main()