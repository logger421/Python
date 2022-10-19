line = """Lorem Ipsum 
    is simply dummy GvR text of 
    the printing and typesetting 
    industry."""

if __name__ == '__main__':
    line1 = " ".join(sorted(line.split(), key=str.lower))
    print(f"Given text sorted alphabetically:\n '{line1}'")
    line2 = " ".join(sorted(line.split(), key=len))
    print(f"Given text sorted by words lengths:\n '{line2}'")