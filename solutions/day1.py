def run():
    task1()
    task2()

def task1():
    max_cal = 0
    with open("inputs/day1task1.txt", "r") as inp:
        cal_sum = 0
        for line in inp:
            if line == "\n":
                max_cal = max(max_cal, cal_sum)
                cal_sum = 0
            else:
                cal_sum += int(line)
    print(max_cal)

def task2():
    max_cal = [0,0,0]
    with open("inputs/day1task1.txt", "r") as inp:
        cal_sum = 0
        for line in inp:
            if line == "\n":
                max_cal.append(cal_sum)
                max_cal.sort(reverse=True)
                max_cal = max_cal[:3]
                cal_sum = 0
            else:
                cal_sum += int(line)
    print(sum(max_cal))

if __name__ == "__main__":
    run()