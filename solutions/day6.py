def run():
    task1()
    task2()

def task1():
    with open("inputs/day6.txt", "r") as inp:
        stream = inp.readline()
        for i in range(13, len(stream)):
            if stream[i] in stream[i-3:i]:
                continue
            else:
                if stream[i-1] in stream[i-3:i-1]:
                    continue
                elif stream[i-2] == stream[i-3]:
                    continue
                else:
                    print(i+1)
                    break

def task2():
    with open("inputs/day6.txt", "r") as inp:
        stream = inp.readline()
        for i in range(13, len(stream)):
            x = True
            for j in range(13):
                if stream[i-j] in stream[i-13:i-j]:
                    x = False
                    break
            if x:
                print(i+1)
                break

if __name__=="__main__":
    run()