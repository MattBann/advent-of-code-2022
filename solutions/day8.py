def run():
    task1()
    task2()

def task1():
    grid = []
    with open("inputs/day8.txt", "r") as inp:
        for line in inp:
            grid.append(list(line.removesuffix("\n")))
    visibles = [[1 if (i==0 or i==len(grid)-1 or j==0 or j==len(grid[0])-1) else 0 for j in range(len(grid[0]))] for i in range(len(grid))]
    for i in range(1,len(visibles)-1):
        for j in range(1,len(visibles[i])-1):
            value = grid[i][j]
            if not sum([1 if grid[a][j] >= value else 0 for a in range(i)]) >= 1:
                visibles[i][j] = 1
                continue
            if not sum([1 if grid[a][j] >= value else 0 for a in range(i+1, len(grid))]) >= 1:
                visibles[i][j] = 1
                continue
            if not sum([1 if grid[i][a] >= value else 0 for a in range(j)]) >= 1:
                visibles[i][j] = 1
                continue
            if not sum([1 if grid[i][a] >= value else 0 for a in range(j+1, len(grid[i]))]) >= 1:
                visibles[i][j] = 1
                continue
            visibles[i][j] = 0
    
    total = 0
    for i in visibles: total += sum(i)
    
    print(total)

def task2():
    grid = []
    with open("inputs/day8.txt", "r") as inp:
        for line in inp:
            grid.append(list(line.removesuffix("\n")))
    print(grid)
    best = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            scoreA, scoreB, scoreC, scoreD = 0,0,0,0
            a,b = i-1,j-1
            value = grid[i][j]
            while a >= 0:
                scoreA += 1
                if grid[a][j] >= value: break
                a-=1
            a = i+1
            while a < len(grid[i]):
                scoreB += 1
                if grid[a][j] >= value: break
                a+=1
            while b >= 0:
                scoreC += 1
                if grid[i][b] >= value: break
                b-=1
            b = j+1
            while b < len(grid[i]):
                scoreD += 1
                if grid[i][b] >= value: break
                b+=1
            best = max(best, scoreA*scoreB*scoreC*scoreD)
        
    print(best)

if __name__=="__main__":
    run()