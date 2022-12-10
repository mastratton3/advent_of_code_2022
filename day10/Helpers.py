
def render_row(l):
    gen = range(0,len(l))
    entries = []
    for i in gen:
        current_val = l[i]
        current_pos = i
        val_to_append = "#" if (current_pos >= (current_val - 1)) and (current_pos <= (current_val + 1)) else "."
        entries.append(val_to_append)
    return "".join(entries)

class CRDT(object):

    def __init__(self):
        self.current_xval = 1
        self.current_cycle = 1
        self.cycle_history = []
        # self.current_command = None

    def __repr__(self):
        return f"CRDT(current_xval={self.current_xval}, current_cycle={self.current_cycle}, cycle_history={self.cycle_history})"

    def parse_instruction(self, input):
        if input == "noop":
            self.run_noop()
        else:
            adx_num = int(input.split(" ")[1])
            self.run_addx(adx_num)

    def run_noop(self):
        self.cycle_history.append(self.current_xval)
        self.current_cycle += 1

    def run_addx(self, adx_num, rem_cycles=2):
        if rem_cycles == 0:
            self.current_xval += adx_num
        else:
            self.cycle_history.append(self.current_xval)
            self.current_cycle += 1
            self.run_addx(adx_num, rem_cycles - 1)

    def calc_signal_strength(self):
        return [(x+1) * self.cycle_history[x] for x in range(0, len(self.cycle_history))]