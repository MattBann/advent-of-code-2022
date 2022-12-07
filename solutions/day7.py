class Dir:
    
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = []
        self.is_dir = True
    
    def update_size(self, size):
        self.size += size
        if self.parent != None:
            self.parent.update_size(size)

class File:

    def __init__(self, name, size, parent) -> None:
        self.name = name
        self.size = size
        self.parent = parent
        self.is_dir = False

        
def run():
    task1()
    task2()

def task1():
    root = Dir("/")
    with open("inputs/day7.txt", "r") as inp:
        curr_dir = root
        for l in inp:
            line = l.removesuffix("\n")
            a = line.split(" ")
            if a[0] == "$":
                if a[1] == "cd":
                    if a[2] == "/": continue
                    elif a[2] == "..":
                        parent = curr_dir.parent
                        curr_dir = parent
                        
                    else:
                        for i in range(len(curr_dir.children)):
                            if curr_dir.children[i].name == a[2]:
                                curr_dir = curr_dir.children[i]
                                break
                elif a[1] == "ls":
                    continue
            elif a[0] == "dir":
                curr_dir.children.append(Dir(a[1], curr_dir))
            else:
                child = File(a[1], int(a[0]), curr_dir)
                curr_dir.children.append(child)
                curr_dir.update_size(child.size)
    
    stack = []
    stack.append(root)
    total = 0
    while (len(stack) != 0):
        node = stack.pop(0)
        if node.is_dir:
            if node.size <= 100000:
                total += node.size
            stack.extend(node.children)
        
    print(total)


def task2():
    root = Dir("/")
    with open("inputs/day7.txt", "r") as inp:
        curr_dir = root
        for l in inp:
            line = l.removesuffix("\n")
            a = line.split(" ")
            if a[0] == "$":
                if a[1] == "cd":
                    if a[2] == "/": continue
                    elif a[2] == "..":
                        parent = curr_dir.parent
                        curr_dir = parent
                        
                    else:
                        for i in range(len(curr_dir.children)):
                            if curr_dir.children[i].name == a[2]:
                                curr_dir = curr_dir.children[i]
                                break
                elif a[1] == "ls":
                    continue
            elif a[0] == "dir":
                curr_dir.children.append(Dir(a[1], curr_dir))
            else:
                child = File(a[1], int(a[0]), curr_dir)
                curr_dir.children.append(child)
                curr_dir.update_size(child.size)
    
    stack = []
    stack.append(root)
    min = 70000000
    to_free = 30000000 - (70000000 - root.size)
    while (len(stack) != 0):
        node = stack.pop(0)
        if node.is_dir:
            if node.size >= to_free:
                if node.size < min:
                    min = node.size
            stack.extend(node.children)
        
    print(min)

if __name__=="__main__":
    run()