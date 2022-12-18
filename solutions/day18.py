from collections import deque

def run():
    task1()
    task2()

def task1():
    cubes = []
    with open("inputs/day18.txt", "r") as inp:
        for line in inp:
            a = line.removesuffix("\n").split(",")
            cubes.append(tuple([int(i) for i in a]))
    
    sa = 0
    for i in cubes:
        if not (i[0]+1, i[1], i[2]) in cubes:
            sa += 1
        if not (i[0]-1, i[1], i[2]) in cubes:
            sa += 1
        if not (i[0], i[1]+1, i[2]) in cubes:
            sa += 1
        if not (i[0], i[1]-1, i[2]) in cubes:
            sa += 1
        if not (i[0], i[1], i[2]+1) in cubes:
            sa += 1
        if not (i[0], i[1], i[2]-1) in cubes:
            sa += 1
    
    print(sa)

def task2():
    cubes = []
    with open("inputs/day18.txt", "r") as inp:
        for line in inp:
            a = line.removesuffix("\n").split(",")
            cubes.append(tuple([int(i) for i in a]))
    
    sa = 0
    
    q = deque()
    q.append((0,0,0))
    curr = set()
    while (len(q) > 0):
        j = q.popleft()
        curr.add(j)

        if j[0] < -1 or j[1] < -1 or j[2] < -1: continue
        if j[0] > 20 and j[1] > 20 and j[2] > 20: break
        if j[0] > 20 or j[1] > 20 or j[2] > 20: continue

        pos = (j[0]+1, j[1], j[2])
        if pos in cubes:
            sa += 1
        elif not pos in curr and not pos in q:
            q.append(pos)
        pos = (j[0]-1, j[1], j[2])
        if pos in cubes:
            sa += 1
        elif not pos in curr and not pos in q:
            q.append(pos)
        pos = (j[0], j[1]+1, j[2])
        if pos in cubes:
            sa += 1
        elif not pos in curr and not pos in q:
            q.append(pos)
        pos = (j[0], j[1]-1, j[2])
        if pos in cubes:
            sa += 1
        elif not pos in curr and not pos in q:
            q.append(pos)
        pos = (j[0], j[1], j[2]+1)
        if pos in cubes:
            sa += 1
        elif not pos in curr and not pos in q:
            q.append(pos)
        pos = (j[0], j[1], j[2]-1)
        if pos in cubes:
            sa += 1
        elif not pos in curr and not pos in q:
            q.append(pos)
    
    print(sa)

if __name__ == "__main__":
    run()