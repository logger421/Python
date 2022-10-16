line = """Lorem Ipsum 
    is simply dummy text of 
    the printing and typesetting 
    industry."""


def count_words(text):
    return len(text.split())

if __name__ == '__main__':
    print('Performing tests')
    assert (count_words("") == 0)
    assert (count_words("one two") == 2)
    assert (count_words("one two three") == 3)
    assert (count_words("one two three four") == 4)
    print('All test succeeded!')

print("Length of given line is equal to: " + str(count_words(line)))
