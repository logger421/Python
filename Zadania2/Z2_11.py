def print_with_underscore(x):
    return str("_".join([ch for ch in x]))

if __name__ == '__main__':
    assert print_with_underscore("word") == "w_o_r_d", "Strings are not equal"
