from Z2_10 import count_words
from Z2_11 import print_with_underscore
from Z2_13 import len_of_words

line = """Lorem Ipsum 
    is simply dummy text of 
    the printing and typesetting 
    industry."""


if __name__ == '__main__':
    print("Length of given line is equal to: " + str(count_words(line)))
    print("String 'word' separated with underscores looks like this: " + print_with_underscore("word"))
    print("All words in given texts have length equal to: " + str(len_of_words(line)))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
