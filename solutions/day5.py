def run():
    task1()
    print("")
    task2()

def task1():
    with open("inputs/day5.txt","r") as inp:
        i = 0
        stacks = [[] for j in range(9)]
        for line in inp:
            if i < 8:
                j = 0
                while j < 9:
                    if line[1+4*j].isalpha():
                        stacks[j].append(line[1+4*j])
                    j+=1
            elif i == 8:
                for j in stacks:
                    j.reverse()
            elif i > 9:
                a = line.split(" ")
                x = int(a[1])
                stack1 = stacks[int(a[3])-1]
                stack2 = stacks[int(a[5])-1]
                for j in range(x):
                    stack2.append(stack1.pop(-1))
            i+=1
        for j in stacks: print(j)

def task2():
    with open("inputs/day5.txt","r") as inp:
        i = 0
        stacks = [[] for j in range(9)]
        for line in inp:
            if i < 8:
                j = 0
                while j < 9:
                    if line[1+4*j].isalpha():
                        stacks[j].append(line[1+4*j])
                    j+=1
            elif i == 8:
                for j in stacks:
                    j.reverse()
            elif i > 9:
                a = line.split(" ")
                x = int(a[1])
                stack1 = stacks[int(a[3])-1]
                stack2 = stacks[int(a[5])-1]
                stack2.extend(stack1[len(stack1)-x:])
                for j in range(x):
                    stack1.pop()
            i+=1
        for j in stacks: print(j)


if __name__=="__main__":
    run()