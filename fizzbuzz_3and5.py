
for i in range(1, 100):
    word = []
    if i % 3 == 0:
        word.append('fizz')
    if i % 5 == 0:
        word.append('buzz')
    if len(word) == 0:
        word.append(str(i))
    print(''.join(word))
