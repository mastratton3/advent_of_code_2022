
from Helpers import *


monkey0 = Monkey([71, 56, 50, 73],
                lambda x: x * 11,
                13,
                {True: "1",
                False: "7"})

monkey1 = Monkey([70, 89, 82],
                lambda x: x + 1,
                7,
                {True: "3",
                False: "6"})

monkey2 = Monkey([52, 95],
                lambda x: x * x,
                3,
                {True: "5",
                False: "4"})

monkey3 = Monkey([94, 64, 69, 87, 70],
                lambda x: x + 2,
                19,
                {True: "2",
                False: "6"})

monkey4 = Monkey([98, 72, 98, 53, 97, 51],
                lambda x: x + 6,
                5,
                {True: "0",
                False: "5"})

monkey5 = Monkey([79],
                lambda x: x + 7,
                2,
                {True: "7",
                False: "0"})

monkey6 = Monkey([77, 55, 63, 93, 66, 90, 88, 71],
                lambda x: x*7,
                11,
                {True: "2",
                False: "4"})

monkey7 = Monkey([54, 97, 87, 70, 59, 82, 59],
                lambda x: x + 8,
                17,
                {True: "1",
                False: "3"})

monkeys = {"0": monkey0,
            "1": monkey1,
            "2": monkey2,
            "3": monkey3,
            "4": monkey4,
            "5": monkey5,
            "6": monkey6,
            "7": monkey7}

def run_round():
    for (monkey_num, monkey) in monkeys.items():
        to_send = monkey.run_all_items()
        process_items_to_send(to_send, monkeys)

for _ in range(0,20):
    run_round()

num_inspected = [v.num_inspected for (k,v) in monkeys.items()]
num1 = max(num_inspected)
num_inspected.remove(num1)
num2 = max(num_inspected)
monkey_business = num1*num2

