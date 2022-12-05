def run():
    task1()
    task2()

def task1():
    count = 0
    with open("inputs/day4.txt", "r") as inp:
        for line in inp:
            a = line.split(",")
            b = a[0].split("-")
            c = a[1].split("-")

            if (int(b[0]) >= int(c[0]) and int(b[1]) <= int(c[1])) or (int(c[0]) >= int(b[0]) and int(c[1]) <= int(b[1])):
                count +=1 
    
    print(count)


def task2():
    count = 0
    with open("inputs/day4.txt", "r") as inp:
        for line in inp:
            a = line.split(",")
            b = a[0].split("-")
            c = a[1].split("-")

            if (int(b[0]) >= int(c[0]) and int(b[1]) <= int(c[1])) or (int(c[0]) >= int(b[0]) and int(c[1]) <= int(b[1])):
                count +=1 
                continue
            if (int(b[0]) >= int(c[0]) and int(b[0]) <= int(c[1])) or (int(b[1]) <= int(c[1]) and int(b[1]) >= int(c[0])):
                count +=1 
    
    print(count)

if __name__=="__main__":
    run()