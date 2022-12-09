def run():
    task1()
    task2()

def task1():
    gridH = []
    gridT = []
    with open("inputs/day9.txt", "r") as inp:
        gridH.append([0,0])
        gridT.append([0,0])
        direction = (0,0)
        for line in inp:
            a = line.removesuffix("\n").split(" ")
            if a[0] == "R": direction = (1,0)
            elif a[0] == "L": direction = (-1,0)
            elif a[0] == "U": direction = (0,1)
            elif a[0] == "D": direction = (0,-1)

            for i in range(int(a[1])):
                prev = gridH[-1]
                new = []
                new.append(prev[0] + direction[0])
                new.append(prev[1] + direction[1])
                gridH.append(new)

                prevT = gridT[-1]
                newT = []
                if new[0] == prevT[0] + (2*direction[0]) and new[1] == prevT[1] + (2*direction[1]):
                    newT.append(prevT[0] + direction[0])
                    newT.append(prevT[1] + direction[1])
                    gridT.append(newT)
                elif (new[0]-prevT[0])**2 + (new[1]-prevT[1])**2 > 2:
                    if direction[0] == 0:
                        newT.append(new[0])
                        newT.append(prevT[1]+direction[1])
                    else:
                        newT.append(prevT[0]+direction[0])
                        newT.append(new[1])
                    gridT.append(newT)
    visited = []
    for i in gridT:
        in_visited = False
        for j in visited:
            if i[0] == j[0] and i[1] == j[1]:
                in_visited = True
        if not in_visited:
            visited.append(i)
    print(len(visited))

# I am highly aware of how inefficient this is, but it seems to work
def move_tail(pos, head):
    if head[0] == pos[0] and abs(head[1]-pos[1]) >= 2:
        return [pos[0], pos[1]+((head[1]-pos[1])//2)]
    elif head[1] == pos[1] and abs(head[0]-pos[0]) >= 2:
        return [pos[0]+((head[0]-pos[0])//2), pos[1]]
    elif (head[0] == pos[0] and head[1] == pos[1]) or (abs(head[0]-pos[0])==1 and abs(head[1]-pos[1])==1):
        return [pos[0], pos[1]]
    elif (abs(head[0]-pos[0])==1 and head[1]==pos[1]) or (abs(head[1]-pos[1])==1 and head[0]==pos[0]):
        return [pos[0], pos[1]]
    elif abs(head[0]-pos[0]) > abs(head[1]-pos[1]):
        return [pos[0]+((head[0]-pos[0])//2), head[1]]
    elif abs(head[1]-pos[1]) > abs(head[0]-pos[0]):
        return [head[0], pos[1]+((head[1]-pos[1])//2)]
    elif abs(head[0]-pos[0]) == abs(head[1]-pos[1]):
        return [pos[0]+((head[0]-pos[0])//2), pos[1]+((head[1]-pos[1])//2)]
    return [pos[0], pos[1]]


def task2():
    gridH = []
    gridT = [[[0,0]] for i in range(9)]
    with open("inputs/day9.txt", "r") as inp:
        gridH.append([0,0])
        direction = (0,0)
        for line in inp:
            a = line.removesuffix("\n").split(" ")
            if a[0] == "R": direction = (1,0)
            elif a[0] == "L": direction = (-1,0)
            elif a[0] == "U": direction = (0,1)
            elif a[0] == "D": direction = (0,-1)

            for i in range(int(a[1])):
                prev = gridH[-1]
                new = []
                new.append(prev[0] + direction[0])
                new.append(prev[1] + direction[1])
                gridH.append(new)
                
                for j in range(9):
                    gridT[j].append(move_tail(gridT[j][-1], new if j==0 else gridT[j-1][-1]))
    
    visited = []
    for i in gridT[-1]:
        in_visited = False
        for j in visited:
            if i[0] == j[0] and i[1] == j[1]:
                in_visited = True
        if not in_visited:
            visited.append(i)
            print(i)
    
    print(len(visited))

if __name__=="__main__":
    run()