def run():
    task1()
    # task2()

shapes = [
    [(0,0),(1,0),(2,0),(3,0)],
    [(1,0),(0,1),(1,1),(2,1),(1,2)],
    [(0,0),(1,0),(2,0),(2,1),(2,2)],
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(0,1),(1,1)]
]

def task1():
    pushes : list
    with open("inputs/day17.txt", "r") as inp:
        pushes = [-1 if i=="<" else 1 for i in inp.read().removesuffix("\n")]
    shape = 0
    push = 0
    i = 0
    max_height = 0
    actual_height = 0
    grid = set()
    while i < 2022:
        x, y = 2, max_height + 4
        falling = True
        s = shapes[shape]
        while falling:
            move = True
            for p in s:
                if x + p[0] + pushes[push] in (-1, 7) or (x+p[0]+pushes[push],y+p[1]) in grid:
                    move = False
                    break
            if move:
                x += pushes[push]
            push = (push + 1) % len(pushes)
            move = True
            for p in s:
                if (x + p[0], y + p[1] - 1) in grid or y + p[1] - 1 <= 0:
                    move = False
                    break
            if move:
                y -= 1
            else:
                for p in s:
                    grid.add((x + p[0], y + p[1]))
                    falling = False
                    max_height = max(max_height, y + p[1])
        i += 1
        shape = (shape + 1) % len(shapes)
    print(actual_height + max_height)

# Task 2 solution does not work - takes way too long
def task2():
    pushes : list
    with open("inputs/day17.txt", "r") as inp:
        pushes = [-1 if i=="<" else 1 for i in inp.read().removesuffix("\n")]
    shape = 0
    push = 0
    i = 0
    max_height = 0
    actual_height = 0
    grid = set()
    while i < 1000000:
        # if (i >> 20) & 1 : print(i)
        x, y = 2, max_height + 4
        falling = True
        s = shapes[shape]
        while falling:
            move = True
            for p in s:
                if x + p[0] + pushes[push] in (-1, 7) or (x+p[0]+pushes[push],y+p[1]) in grid:
                    move = False
                    break
            if move:
                x += pushes[push]
            push = (push + 1) % len(pushes)
            move = True
            for p in s:
                if (x + p[0], y + p[1] - 1) in grid or y + p[1] - 1 <= 0:
                    move = False
                    break
            if move:
                y -= 1
            else:
                for p in s:
                    grid.add((x + p[0], y + p[1]))
                    falling = False
                    max_height = max(max_height, y + p[1])
                for h in range(max_height-10, max_height+1):
                    if len([j for j in grid if j[1] == h]) == 7:
                        # print([j for j in grid if j[1] == h])
                        grid = set([(j[0], j[1]-h) for j in grid if j[1] > h])
                        actual_height += h
                        # print("Prev max:", max_height)
                        max_height -= h
                        # print("Reset", actual_height, max_height)
                        break
            # print(x,y)
        i += 1
        shape = (shape + 1) % len(shapes)
        # print(sorted(grid))
        # print(max_height)
        # input()
    print(actual_height + max_height)
            

if __name__ == "__main__":
    run()