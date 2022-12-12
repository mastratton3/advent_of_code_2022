import math
from functools import reduce

def process_items_to_send(items_to_send, monkey_dict):
    for (monkey_num, items) in items_to_send.items():
        [monkey_dict[monkey_num].accept_item(x) for x in items]

master_divisor = math.lcm(*[13, 7, 3, 19, 5, 2, 11, 17])

class Monkey(object):

    def __init__(self, starting_items, monkey_func, monkey_test, toss_to):
        self.items = starting_items
        self.monkey_func = monkey_func
        self.monkey_test = monkey_test
        self.toss_to = toss_to
        self.num_inspected = 0

    def accept_item(self, item):
        self.items.append(item)

    def run_test(self, input):
        return (input % self.monkey_test) == 0

    def process_item(self):
        item_to_proc = self.items.pop(0)
        new_item_val = self.monkey_func(item_to_proc) % master_divisor
        self.num_inspected += 1
        return (self.toss_to[self.run_test(new_item_val)], new_item_val)

    def run_all_items(self):
        items_to_send = {}
        for _ in range(0, len(self.items)):
            res = self.process_item()
            if res[0] in items_to_send.keys():
                items_to_send[res[0]].append(res[1])
            else:
                items_to_send[res[0]] = [res[1]]
        return items_to_send
