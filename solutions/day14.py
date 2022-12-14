def run():
    task1()
    task2()

def task1():
    grid = [[0 for i in range(600)] for j in range(200)]
    with open("inputs/day14.txt", "r") as inp:
        for line in inp:
            a = line.removesuffix("\n").split(" -> ")
            for i in range(len(a)-1):
                b = [int(j) for j in a[i].split(",")]
                c = [int(j) for j in a[i+1].split(",")]
                if b[0] == c[0]:
                    for j in range(min(b[1],c[1]), max(b[1],c[1])+1):
                        grid[j][b[0]] = 1
                else:
                    for j in range(min(b[0],c[0]), max(b[0],c[0])+1):
                        grid[b[1]][j] = 1
    
    count = 0
    end = False
    while not end:
        sandx = 500
        sandy = 0
        settled = False
        while not settled:
            if sandy+1 >= len(grid):
                end = True
                break
            if grid[sandy+1][sandx] == 0:
                sandy = sandy+1
            elif grid[sandy+1][sandx-1] == 0:
                sandy = sandy+1
                sandx = sandx-1
            elif grid[sandy+1][sandx+1] == 0:
                sandy = sandy+1
                sandx = sandx+1
            else:
                settled = True
                grid[sandy][sandx] = 2
                count += 1
    print(count)

def task2():
    grid = [[0 for i in range(1000)] for j in range(200)]
    max_y = 0
    with open("inputs/day14.txt", "r") as inp:
        for line in inp:
            a = line.removesuffix("\n").split(" -> ")
            for i in range(len(a)-1):
                b = [int(j) for j in a[i].split(",")]
                c = [int(j) for j in a[i+1].split(",")]
                max_y = max(max_y, b[1])
                max_y = max(max_y, c[1])
                if b[0] == c[0]:
                    for j in range(min(b[1],c[1]), max(b[1],c[1])+1):
                        grid[j][b[0]] = 1
                else:
                    for j in range(min(b[0],c[0]), max(b[0],c[0])+1):
                        grid[b[1]][j] = 1
    grid[max_y+2] = [1 for i in range(len(grid[0]))]
    
    count = 0
    end = False
    while not end:
        sandx = 500
        sandy = 0
        settled = False
        while not settled:
            if grid[sandy+1][sandx] == 0:
                sandy = sandy+1
            elif grid[sandy+1][sandx-1] == 0:
                sandy = sandy+1
                sandx = sandx-1
            elif grid[sandy+1][sandx+1] == 0:
                sandy = sandy+1
                sandx = sandx+1
            else:
                settled = True
                grid[sandy][sandx] = 2
                count += 1
                if sandx == 500 and sandy == 0:
                    end = True
                    break
    print(count)

if __name__=="__main__":
    run()