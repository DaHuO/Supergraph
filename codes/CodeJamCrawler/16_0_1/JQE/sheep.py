import math

input = open("A-large.in", "r")
cases = int(input.readline())
start = [0,0,0,0,0,0,0,0,0,0]
def done(p):
    for i in p:
        if i < 1:
            return False
    return True

for case in range(cases):
    progress = start[:]
    N = int(input.readline())
    if N == 0:
        print("Case #{0}: INSOMNIA".format(case+1))
        continue
    solution = N
    num = N
    while not done(progress):
        power = 0
        while(True):
            m = math.pow(10, power + 1)
            d = math.pow(10, power)
            if d > num:
                break
            progress[int((num % m) // d)] = 1
            power += 1
        solution = num
        num = num + N
    print("Case #{0}: {1}".format(case+1, solution))