from itertools import islice


def four_chars_are_diff(s, w=4):
    return len(set(s)) == w

def slice_iterate(l, window=4):
    for i in range(0, len(l)):
        current_window = l[i:i+window]
        if len(current_window) == window:
            yield current_window

def slice_and_check_diff(l, window=4):
    return [four_chars_are_diff(x, window) for x in slice_iterate(l, window)]

def len_to_first(s, w=4):
    truth_test = slice_and_check_diff(s, w)
    num_false = 0
    keep_checking = True
    for x in truth_test:
        if keep_checking:
            if not x:
                num_false +=1
            else:
                keep_checking = False
    return num_false + w

def len_to_som(s):
    return len_to_first(s, 14)