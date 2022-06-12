import random
from linecache import getline


def random_word():
    f = open('wordList.txt')
    count = 0
    for i in f:
        count += 1

    random_number = random.randint(1, count)

    word = getline('wordList.txt', random_number)
    f.close()
    return word
