from dwa_10 import count_words

if __name__ == '__main__':
    print('Performing tests')
    assert (count_words("") == 0)
    assert (count_words("one two") == 2)
    assert (count_words("one two three") == 3)
    assert (count_words("one two three four") == 4)
    print('All test succeeded!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
