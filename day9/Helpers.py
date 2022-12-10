

class Pos(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def are_adjacent(self, other):
        delta_x = abs(self.x - other.x)
        delta_y = abs(self.y - other.y)
        return delta_x <= 1 and delta_y <= 1

    def __repr__(self):
        return f"Pos(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __getitem__(self, pos):
        if pos == 0:
            return self.x
        elif pos == 1:
            return self.y

    def __add__(self, other):
        return Pos(self.x + other[0], self.y + other[1])

    def __sub__(self, other):
        return Pos(self.x - other[0], self.y - other[1])

x_change_dict = {"L": -1,
                "R": 1,
                "D": 0,
                "U": 0}

y_change_dict = {"L": 0,
                "R": 0,
                "D": -1,
                "U": 1}

# Very ugly function
def determine_move(h_t_delta: Pos):
    if h_t_delta.x > 1:
        x_change = 1
    elif h_t_delta.x < -1:
        x_change = -1
    elif abs(h_t_delta.y) > 1:
        x_change = h_t_delta.x
    else:
        x_change = 0
    if h_t_delta.y > 1:
        y_change = 1
    elif h_t_delta.y < -1:
        y_change = -1
    elif abs(h_t_delta.x) > 1:
        y_change = h_t_delta.y
    else:
        y_change = 0
    return Pos(x_change, y_change)

class GameBoard(object):

    def __init__(self, tail_length=1):
        self.hpos = Pos(0,0)
        self.tpos = [Pos(0,0) for _ in range(0, tail_length)]
        self.tail_visits = set([self.tpos[-1]])
        self.tail_length=tail_length

    def __repr__(self):
        return f"GameBoard(hpos={self.hpos}, tpos={self.tpos}, tail_visits={self.tail_visits})"

    def are_adjacent(self):
        pass

    def move_h(self, direction, num_times=1):
        x_change = x_change_dict[direction]
        y_change = y_change_dict[direction]
        self.hpos = self.hpos + (x_change, y_change)
        self.move_t(0)
        num_times -= 1
        if num_times > 0:
            self.move_h(direction, num_times)

    def move_t(self, entry):
        head_to_use = self.hpos if entry == 0 else self.tpos[entry - 1]
        h_t_delta = head_to_use - self.tpos[entry]
        move = determine_move(h_t_delta)
        self.tpos[entry] = self.tpos[entry] + move
        if entry + 1 == self.tail_length:
            self.tail_visits.add(self.tpos[-1])
        else:
            self.move_t(entry + 1)



