from collections import deque

class Node:
    def __init__(self, height, x, y) -> None:
        self.height = height
        self.x = x
        self.y = y
        self.prev : Node
        self.dist = 999999999
        self.visited = False

def run():
    task1()
    task2()

def task1():
    grid = []
    q = deque()
    x = 0
    end = None
    with open("inputs/day12.txt", "r") as inp:
        for line in inp:
            a = list(line.removesuffix("\n"))
            grid.append([Node(ord(a[i])-ord("a"),x, i) for i in range(len(a))])
            for i in range(len(a)):
                if a[i] == "S":
                    grid[x][i].height = 0
                    grid[x][i].dist = 0
                    q.append(grid[x][i])
                elif a[i] == "E":
                    grid[x][i].height = ord("z") - ord("a")
                    end = grid[x][i]
            x+=1
    
    best = 999999999
    while len(q) > 0:
        node :Node= q.popleft()
        node.visited = True
        b : Node
        if node.x > 0:
            b = grid[node.x-1][node.y]
            if b.height <= node.height+1 and not b.visited:
                if b.dist > node.dist+1:
                    b.dist = node.dist+1
                    b.prev = node
                    if b is end:
                        best = b.dist
                        break
                if not b in q:
                    q.append(b)
        if node.x < len(grid)-1:
            b = grid[node.x+1][node.y]
            if b.height <= node.height+1 and not b.visited:
                if b.dist > node.dist+1:
                    b.dist = node.dist+1
                    b.prev = node
                    if b is end:
                        best = b.dist
                        break
                if not b in q:
                    q.append(b)
        if node.y > 0:
            b = grid[node.x][node.y-1]
            if b.height <= node.height+1 and not b.visited:
                if b.dist > node.dist+1:
                    b.dist = node.dist+1
                    b.prev = node
                    if b is end:
                        best = b.dist
                        break
                if not b in q:
                    q.append(b)
        if node.y < len(grid[0])-1:
            b = grid[node.x][node.y+1]
            if b.height <= node.height+1 and not b.visited:
                if b.dist > node.dist+1:
                    b.dist = node.dist+1
                    b.prev = node
                    if b is end:
                        best = b.dist
                        break
                if not b in q:
                    q.append(b)
        
    print(best)

def task2():
    grid = []
    q = deque()
    x = 0
    end = None
    with open("inputs/day12.txt", "r") as inp:
        for line in inp:
            a = list(line.removesuffix("\n"))
            grid.append([Node(ord(a[i])-ord("a"),x, i) for i in range(len(a))])
            for i in range(len(a)):
                if a[i] == "E":
                    grid[x][i].height = ord("z") - ord("a")
                    grid[x][i].dist = 0
                    q.append(grid[x][i])
                elif a[i] == "S":
                    grid[x][i].height = 0
            x+=1
    
    best = 999999999
    while len(q) > 0:
        node :Node= q.popleft()
        node.visited = True
        b : Node
        if node.x > 0:
            b = grid[node.x-1][node.y]
            if b.height >= node.height-1 and not b.visited:
                if b.dist > node.dist+1:
                    b.dist = node.dist+1
                    b.prev = node
                    if b.height == 0:
                        best = b.dist
                        break
                if not b in q:
                    q.append(b)
        if node.x < len(grid)-1:
            b = grid[node.x+1][node.y]
            if b.height >= node.height-1 and not b.visited:
                if b.dist > node.dist+1:
                    b.dist = node.dist+1
                    b.prev = node
                    if b.height == 0:
                        best = b.dist
                        break
                if not b in q:
                    q.append(b)
        if node.y > 0:
            b = grid[node.x][node.y-1]
            if b.height >= node.height-1 and not b.visited:
                if b.dist > node.dist+1:
                    b.dist = node.dist+1
                    b.prev = node
                    if b.height == 0:
                        best = b.dist
                        break
                if not b in q:
                    q.append(b)
        if node.y < len(grid[0])-1:
            b = grid[node.x][node.y+1]
            if b.height >= node.height-1 and not b.visited:
                if b.dist > node.dist+1:
                    b.dist = node.dist+1
                    b.prev = node
                    if b.height == 0:
                        best = b.dist
                        break
                if not b in q:
                    q.append(b)
        
    print(best)

if __name__=="__main__":
    run()