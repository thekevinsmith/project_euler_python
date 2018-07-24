# Problem 5 : Statement:
# 2520 is the smallest number that can be divided by each of
# the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?
#16@720720
#17@5045040
#18@12252240
#19@
#20@232792560

def main():

    start = 1
    limit = 20
    endpoint = 100000000000
    output = 0
    numbers = []
    endloop = False

    for n in range(start, endpoint, 1):
        for i in range(start, (limit + 1), 1):
            if n % i == 0:
                numbers.append(i)
                if len(numbers) == limit:
                    output = n
                    endloop = True
                    break
                else:
                    continue
            else:
                numbers = []
        if endloop:
            break
        else:
            continue

    print(numbers)
    print(len(numbers))
    print(output)


if __name__ == '__main__':
    main()