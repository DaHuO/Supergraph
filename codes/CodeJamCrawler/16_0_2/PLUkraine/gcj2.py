def allPlus(pans):
    return all(x == '+' for x in pans)


def turn(pans, i):
    return ''.join(['+' if x == '-' else '-' for x in pans[i-1::-1]]) + pans[i:]


def turnsNum(pans):
    n = len(pans)
    last_i = 1
    steps = 0
    while not allPlus(pans):
        for i in range(last_i, n):
            # check if all before i are the same
            if pans[i] != pans[i-1]:
                pans = turn(pans, i)
                last_i = i+1
                steps += 1
                break
        else:
            pans = turn(pans, n)
            steps += 1
    return steps

T = int(input())
for i in range(T):
    inPans = input()
    print("Case #{0}: {1}".format(i+1, turnsNum(inPans)))
