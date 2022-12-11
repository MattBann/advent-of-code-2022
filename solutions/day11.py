from collections import deque

class Monkey:
    def __init__(self, number) -> None:
        self.number = number
        self.items = deque()
        self.test = 1
        self.operation = 1
        self.operand = 0
        self.true_dest = number
        self.false_dest = number
        self.inspections = 0

def run():
    task1()
    task2()

def task1():
    monkeys = []
    with open("inputs/day11.txt", "r") as inp:
        i = -1
        for line in inp:
            a = line.removesuffix("\n").split(" ")
            if line.removesuffix("\n") == "": continue
            if a[0] == "Monkey":
                i += 1
                monkeys.append(Monkey(i))
            elif a[2] == "Starting":
                items = [int(i.removesuffix(",")) for i in a[4:]]
                monkeys[i].items.extend(items)
            elif a[2] == "Operation:":
                if a[6] == "+":
                    monkeys[i].operation = 1
                elif a[6] == "*":
                    monkeys[i].operation = 0
                if a[7] == "old":
                    monkeys[i].operation = 2
                else:
                    monkeys[i].operand = int(a[7])
            elif a[2] == "Test:":
                monkeys[i].test = int(a[5])
            elif a[4] == "If":
                if a[5] == "true:":
                    monkeys[i].true_dest = int(a[9])
                else:
                    monkeys[i].false_dest = int(a[9])
    
    for i in range(20):
        for j in range(len(monkeys)):
            while len(monkeys[j].items) > 0:
                item = monkeys[j].items.popleft()
                if monkeys[j].operation == 0:
                    item *= monkeys[j].operand
                elif monkeys[j].operation == 1:
                    item += monkeys[j].operand
                else:
                    item *= item
                item //= 3
                if item % monkeys[j].test == 0:
                    monkeys[monkeys[j].true_dest].items.append(item)
                else:
                    monkeys[monkeys[j].false_dest].items.append(item)
                monkeys[j].inspections += 1
    
    inspections = sorted([i.inspections for i in monkeys])
    inspections.reverse()
    print(inspections[0]*inspections[1])


def task2():
    monkeys = []
    mult = 1
    with open("inputs/day11.txt", "r") as inp:
        i = -1
        for line in inp:
            a = line.removesuffix("\n").split(" ")
            if line.removesuffix("\n") == "": continue
            if a[0] == "Monkey":
                i += 1
                monkeys.append(Monkey(i))
            elif a[2] == "Starting":
                items = [int(i.removesuffix(",")) for i in a[4:]]
                monkeys[i].items.extend(items)
            elif a[2] == "Operation:":
                if a[6] == "+":
                    monkeys[i].operation = 1
                elif a[6] == "*":
                    monkeys[i].operation = 0
                if a[7] == "old":
                    monkeys[i].operation = 2
                else:
                    monkeys[i].operand = int(a[7])
            elif a[2] == "Test:":
                monkeys[i].test = int(a[5])
                mult *= int(a[5])
            elif a[4] == "If":
                if a[5] == "true:":
                    monkeys[i].true_dest = int(a[9])
                else:
                    monkeys[i].false_dest = int(a[9])
    
    for i in range(10000):
        for j in range(len(monkeys)):
            while len(monkeys[j].items) > 0:
                item = monkeys[j].items.popleft()
                if monkeys[j].operation == 0:
                    item *= monkeys[j].operand
                elif monkeys[j].operation == 1:
                    item += monkeys[j].operand
                else:
                    item *= item
                item %= mult    # Optimisation to reduce time taken for test
                if item % monkeys[j].test == 0:
                    monkeys[monkeys[j].true_dest].items.append(item)
                else:
                    monkeys[monkeys[j].false_dest].items.append(item)
                monkeys[j].inspections += 1
    
    inspections = sorted([i.inspections for i in monkeys])
    inspections.reverse()
    print(inspections[0]*inspections[1])

if __name__=="__main__":
    run()