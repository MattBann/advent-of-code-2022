# This one is rather slow to run
def run():
    task1()
    task2()

def task1():
    points = []
    beacs = []
    y = 2000000
    with open("inputs/day15.txt", "r") as inp:
        for line in inp:
            a = line.removesuffix("\n").split(" ")
            b = a[2].split("=")
            sensx = int(b[1].strip(",:"))
            b = a[3].split("=")
            sensy = int(b[1].strip(",:"))
            b = a[8].split("=")
            beacx = int(b[1].strip(",:"))
            b = a[9].split("=")
            beacy = int(b[1].strip(",:"))
            rad = abs(sensx-beacx) + abs(sensy-beacy)
            points.append((sensx, sensy, rad))
            if beacy == y:
                beacs.append((beacx, beacy))
    
    count = 0
    x = -2000000
    while x < 5000000:
        if (x,y) in beacs:
            x+=1
            continue
        for i in points:
            if abs(i[0]-x) + abs(i[1]-y) <= i[2]:
                count += 1
                break
        x += 1

    print(count)

def task2():
    points = []
    with open("inputs/day15.txt", "r") as inp:
        for line in inp:
            a = line.removesuffix("\n").split(" ")
            b = a[2].split("=")
            sensx = int(b[1].strip(",:"))
            b = a[3].split("=")
            sensy = int(b[1].strip(",:"))
            b = a[8].split("=")
            beacx = int(b[1].strip(",:"))
            b = a[9].split("=")
            beacy = int(b[1].strip(",:"))
            rad = abs(sensx-beacx) + abs(sensy-beacy)
            points.append((sensx, sensy, rad))
    
    y = 0
    while y <= 4000000:
        x = 0
        while x <= 4000000:
            found = True
            for i in points:
                if abs(i[0]-x) + abs(i[1]-y) <= i[2]:
                    x = i[0] + (i[2] - abs(i[1]-y))
                    found = False
                    break
            if found:
                print((x*4000000)+y)
                exit()
            x += 1
        y += 1


if __name__ == "__main__":
    run()