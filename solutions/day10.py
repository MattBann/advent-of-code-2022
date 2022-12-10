def run():
    task1()
    task2()

def cycle(clock, x, outputs):
    if (clock-20) % 40 == 0:
        outputs.append(clock*x)
    return clock+1

def task1():
    with open("inputs/day10.txt", "r") as inp:
        clock = 1
        x = 1
        outputs = []
        for line in inp:
            a = line.removesuffix("\n").split(" ")
            if a[0] == "noop":
                clock = cycle(clock, x, outputs)
            elif a[0] == "addx":
                clock = cycle(clock, x, outputs)
                clock = cycle(clock, x, outputs)
                x += int(a[1])
        
        print(sum(outputs))


def cycle2(clock, x):
    if clock % 40 == 0:
        print("")
    if clock % 40 == x:
        print("#", end="")
    elif clock % 40 == x-1:
        print("#", end="")
    elif clock % 40 == x+1:
        print("#", end="")
    else:
        print(".", end="")
    return clock+1

def task2():
    with open("inputs/day10.txt", "r") as inp:
        clock = 0
        x = 1
        for line in inp:
            a = line.removesuffix("\n").split(" ")
            if a[0] == "noop":
                clock = cycle2(clock, x)
            elif a[0] == "addx":
                clock = cycle2(clock, x)
                clock = cycle2(clock, x)
                x += int(a[1])
        

if __name__=="__main__":
    run()