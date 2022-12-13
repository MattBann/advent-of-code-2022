def run():
    task1()
    task2()

skip = False
def compare(pair):
    global skip
    for i in range(len(pair[0])):
        skip = False
        if i > len(pair[1])-1:
            return False
        if isinstance(pair[0][i], list) and isinstance(pair[1][i], list):
            result = compare([pair[0][i], pair[1][i]])
            if skip : continue
            return result
        elif isinstance(pair[0][i], list) and isinstance(pair[1][i], int):
            result = compare([pair[0][i], [pair[1][i]]])
            if skip : continue
            return result
        elif isinstance(pair[1][i], list) and isinstance(pair[0][i], int):
            result = compare([[pair[0][i]], pair[1][i]])
            if skip : continue
            return result
        else:
            if pair[0][i] > pair[1][i]:
                return False
            if pair[0][i] < pair[1][i]:
                return True
            else: continue
    
    if len(pair[0])==len(pair[1]):
        skip = True
        return True
    else:
        return True


def task1():
    current = []
    i = 1
    sum = 0
    with open("inputs/day13.txt", "r") as inp:
        for line in inp:
            if len(current) < 2:
                eval("current.append({})".format(line.removesuffix("\n")))
            else:
                if compare(current): 
                    sum += i 
                current.clear()
                i+=1
        print(sum)

def task2():
    packets = []
    with open("inputs/day13.txt", "r") as inp:
        for line in inp:
            if line.removesuffix("\n") == "":
                continue
            eval("packets.append({})".format(line.removesuffix("\n")))
    
    packets.append([[2]])
    packets.append([[6]])

    for i in range(len(packets)-1):
        for j in range(len(packets)-i-1):
            if not compare([packets[j], packets[j+1]]):
                temp = packets[j]
                packets[j] = packets[j+1]
                packets[j+1] = temp

    key = 1
    for i in range(len(packets)):
        if packets[i] == [[2]] or packets[i] == [[6]]:
            key *= i+1
    print(key)


if __name__=="__main__":
    run()