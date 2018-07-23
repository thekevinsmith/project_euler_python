# Problem 4 : Statement:
# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def main():
    largest = 0
    for i in range(0, 1000, 1):

        count = 0
        Num = i

        while Num > 0:
            Num = Num//10
            count += 1

        if count == 3:
            prodNum.append(i)

    for p in range(len(prodNum)):
        for n in range(len(prodNum)):
            result = prodNum[p] * prodNum[n]

            test = result
            count = 0

            while test > 0:
                test = test // 10
                count += 1
            if count == 6:
                sixNum.append(result)
                if (result // 10 ** 5 % 10) == (result // 10 ** 0 % 10):
                    if (result // 10 ** 4 % 10) == (result // 10 ** 1 % 10):
                        if (result // 10 ** 3 % 10) == (result // 10 ** 2 % 10):
                            palindromeNum.append(result)    # all that fit criteria
                            if result > largest:
                                largest = result

    print(largest)









if __name__ == '__main__':
    palindromeNum = []
    prodNum = []
    sixNum = []
    main()




    # 994009

    # largest = 0
    # count = 6
    # result = 994009
    # for c in range(0, count // 2, 1):
    #     if (result // 10 ** (count - 1 - c) % 10) == (result // 10 ** (c) % 10):
    #         if result > largest:
    #             largest = result
    # print(result)
    #
    # print(994009// 10**(6-1-0) % 10)# MS
    # print(994009 // 10 ** (0) % 10) # LS
    #
    # print(994009 // 10 ** (6 - 1 - 1) % 10)
    # print(994009 // 10 ** (1) % 10)


