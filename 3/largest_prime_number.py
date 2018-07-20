# Problem 3 : Statement:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# TODO: ALL

# prime numbers are numbers that are only divisible by 1 and itself. THUS:

primenumbers = []
def main(k, N):
    #print(k, N)

    if N == 1:
        return

    if N < k:
        return

    if N % k == 0:
        print(k)  # TODO: prime factoring is working but we need to create an array and not insert duplicates so :
                    # TODO: Check if array[i] != array[(i-1)]: array.append(k), i += 1
        if k != 1:
            return main(k, N / k)  # 3, 15
        else:
            return main(k+1, N/k)   # 3, 15
    else:
        return main(k+1, N)

if __name__ == '__main__':
    main(1, 27)




# primenumbers = []
# div_num = []
# ulti = 250
# for i in range(1, (ulti +1), 1):
#     if ulti % i == 0:
#         div_num.append(i)
#         for j in range(1, (i + 1), 1):
#             if i % j == 0:
#                 primenumbers.append(i)
#                 print(primenumbers)


# for j in range(1, (ulti +1), 1):
#     if ulti % j == 0:
#         print(j)
#         primenumbers.append(j)
#         print(primenumbers)

        #for k in range(len(div_num)):
            #div_num[k] %
        #for j in range(1, i, 1):
            #if i % j == 0:
                #print()


    #print(i)
    #print(div_num)
    #print(primenumbers)