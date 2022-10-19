def len_of_words(text):
    return sum([len(word) for word in text.split()])

line = """Lorem Ipsum 
    is simply dummy text of 
    the printing and typesetting 
    industry."""

if __name__ == '__main__':
    assert len_of_words(line) == 63