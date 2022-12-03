def run():
    task1()
    task2()

def task1():
    priorities = 0
    with open("inputs/day3.txt", "r") as inp:
        for line in inp:
            a = line[:(len(line)//2)]
            b = line[(len(line)//2):]

            for i in a:
                if i in b:
                    if ord(i) <= ord("z") and ord(i) >= ord("a"):
                        priorities += ord(i) - ord("a") + 1
                        break
                    elif ord(i) <= ord("Z") and ord(i) >= ord("A"):
                        priorities += ord(i) - ord("A") + 27
                        break
    print(priorities)

def task2():
    priorities = 0
    j = 0
    a,b,c = "","",""
    with open("inputs/day3.txt", "r") as inp:
        for line in inp:
            if j % 3 == 0:
                a = line
            elif j % 3 == 1:
                b = line
            elif j % 3 == 2:
                c = line

                for i in a:
                    if i in b and i in c:
                        if ord(i) <= ord("z") and ord(i) >= ord("a"):
                            priorities += ord(i) - ord("a") + 1
                            break
                        elif ord(i) <= ord("Z") and ord(i) >= ord("A"):
                            priorities += ord(i) - ord("A") + 27
                            break
            j+=1
    print(priorities)

if __name__=="__main__":
    run()