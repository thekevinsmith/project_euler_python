# Problem statement:
# Print the numbers 1 to 100.
# For every multiple divisible by 3, print fizz
# For every multiple divisible by 5, print buzz
# For multiples divisible by both, print fizzbuzz


def main():

    for i in range(1, 100):
        word = []
        if i % 3 == 0:
            word.append('fizz')
        if i % 5 == 0:
            word.append('buzz')
        if len(word) == 0:
            word.append(str(i))
        print(''.join(word))


if __name__ == '__main__':
    main()