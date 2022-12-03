def run():
    task1()
    task2()

def task1():
    score = 0
    with open("inputs/day2.txt", "r") as inp:
        for line in inp:
            a = line[0]
            b = line[2]
            if a == "A":
                if b == "X":
                    score += 4
                elif b == "Y":
                    score += 8
                else:
                    score += 3
            elif a == "B":
                if b == "X":
                    score += 1
                elif b == "Y":
                    score += 5
                else:
                    score += 9
            elif a == "C":
                if b == "X":
                    score += 7
                elif b == "Y":
                    score += 2
                else:
                    score += 6
    print(score)

def task2():
    score = 0
    with open("inputs/day2.txt", "r") as inp:
        for line in inp:
            a = line[0]
            b = line[2]
            if a == "A":
                if b == "X":
                    score += 3
                elif b == "Y":
                    score += 4
                else:
                    score += 8
            elif a == "B":
                if b == "X":
                    score += 1
                elif b == "Y":
                    score += 5
                else:
                    score += 9
            elif a == "C":
                if b == "X":
                    score += 2
                elif b == "Y":
                    score += 6
                else:
                    score += 7
    print(score)

if __name__=="__main__":
    run()