class MyError(Exception):
    """Warto stworzyć wiersz dokumentujący."""
    pass

if __name__ == '__main__':
    # raise MyError("message")  # wywołanie wyjątku
    exception = MyError("a", "b")  # instancja wyjątku
    print(exception.args)  # ('a', 'b')
    print(exception)  # ('a', 'b')