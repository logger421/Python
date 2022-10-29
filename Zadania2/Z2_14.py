def find_biggest_word(x):
    return max(x.split(), key=len)


def find_biggest_word_len(x):
    return len(find_biggest_word(x))


line = """Lorem Ipsum 
    is simply dummy text of 
    the printing and typesetting 
    industry."""

if __name__ == '__main__':
    print(f"The biggest word in given text is: '{str(find_biggest_word(line))}'")
    print("Length of the biggest word in given text equals: " + str(find_biggest_word_len(line)))