def string_from_beginning(line):
    line = line.split()
    s = [x[0] for x in line]
    return "".join(s)


def string_from_ending(line):
    line = line.split()
    s = [x[-1] for x in line]
    return "".join(s)


line = """Lorem Ipsum 
    is simply dummy text of 
    the printing and typesetting 
    industry."""

if __name__ == '__main__':
    assert string_from_beginning(line) == 'LIisdtotpati'
    assert string_from_ending(line) == 'mmsyytfegdg.'
