if __name__ == '__main__':
    myDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    print(myDict["D"])
    myDict = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)])
    print(myDict["M"])
    del myDict
    myDict["I"] = 1
    myDict["V"] = 5
    myDict["X"] = 10
    myDict["L"] = 50
    myDict["C"] = 100
    myDict["D"] = 500
    myDict["M"] = 1000