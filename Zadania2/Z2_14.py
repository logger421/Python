def find_biggest_word(x):
    return max(x.split())


def find_biggest_word_len(x):
    return len(max(x.split()))


line = """Lorem Ipsum 
    is simply dummy text of 
    the printing and typesetting 
    industry."""

if __name__ == '__main__':
    print("The biggest word in\n" + line + "is: " + str(find_biggest_word(line)))
    print("Length of the biggest word in" + line + "equals: " + str(find_biggest_word_len(line)))