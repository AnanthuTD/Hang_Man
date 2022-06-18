import random
import sys
from linecache import getline
import os


def random_word():
    """word_list = 'wordList.txt'
    if '_MEIPASS2' in os.environ:
        word_list = os.path.join(os.environ['_MEIPASS2'], word_list)"""
    try:
        os.chdir(sys._MEIPASS)
        data_path = 'wordList.txt'
    except AttributeError:
        f = open('wordList.txt')
    else:
        f = open(data_path)
    count = 0
    for i in f:
        count += 1

    random_number = random.randint(1, count)

    word = getline('wordList.txt', random_number)
    f.close()
    return word
