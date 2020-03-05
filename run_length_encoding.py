def run_length_encoding(input_string):
    x = [None, None]
    [x.__setitem__(-1, x[-1]+1) if c == x[-2] else x.extend([c, 1]) for c in input_string]
    return " ".join(map(str, x[2:]))
