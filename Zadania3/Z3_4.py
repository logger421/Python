if __name__ == '__main__':
    while True:
        x = input("Enter a digit or type 'stop' to end: ")
        if x == 'stop':
            print("Cya!")
            break
        else:
            try:
                x = float(x)
            except ValueError:
                print("This isn't valid number!")
                continue
            print("{:10} {:10}".format(x, pow(x, 3)))



