

class Forest(object):

    def __init__(self):
        self.rows = {}

    def add_row(self, row):
        next_row_num = max(self.rows.keys()) + 1 if len(self.rows) > 0 else 0
        self.rows[next_row_num] = row

    def __getitem__(self, elem):
        return self.rows[elem]

    def calc_num_columns(self):
        return len(self.rows[0])

    def __len__(self):
        return len(self.rows)

    def pull_column(self, col_no):
        return [v[col_no] for (k, v) in self.rows.items()]

    def check_visibility(self, row, col):
        row_check_forward = find_visible(self[row])
        row_check_backwards = reverse_list(find_visible(reverse_list(self[row])))
        row_check = consolidate_two_booleans(row_check_forward, row_check_backwards)[col]
        column = self.pull_column(col)
        col_check_forward = find_visible(column)
        col_check_backwards = reverse_list(find_visible(reverse_list(column)))
        col_check = consolidate_two_booleans(col_check_forward, col_check_backwards)[row]
        return row_check or col_check

    def full_visibility_table(self):
        row_gen = range(0, len(self))
        col_gen = range(0, self.calc_num_columns())
        return [self.check_visibility(row, col) for row in row_gen for col in col_gen]

    def visibility_count(self):
        return sum([1 if x else 0 for x in self.full_visibility_table()])


def find_visible(l):
    '''
    Determines which 'numbers are greater than the ones previously seen

    Args:
        l ([int]): List of ints. 

    Returns:
        [Boolean]
    '''
    largest_seen = None
    res = []
    for elem in l:
        if largest_seen is None:
            res.append(True)
            largest_seen = elem
        else:
            is_larger = elem > largest_seen
            if is_larger:
                largest_seen = elem
                res.append(True)
            else:
                res.append(False)
    return res

def consolidate_two_booleans(l1, l2):
    return [l1[x] or l2[x] for x in range(0,len(l1))]

def reverse_list(l):
    l = l.copy()
    l.reverse()
    return l
