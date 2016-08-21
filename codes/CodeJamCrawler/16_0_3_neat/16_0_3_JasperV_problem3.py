import random
import math
def findSolution(n, j):
    solution = []
    while len(solution) < j:
        sol = "1"
        for i in range(n-2):
            sol += str(random.randint(0,1))
        sol += "1"
#        print("s", sol)
        transformed = []
        result = []
        ok = True
        for i in range(2,11):
            transformed.append(int(sol, i))
        for i in transformed:
            fl = int(math.floor(math.pow(i, 1/2)))
            done = False
            for check in range(2,fl+1):
                if i%check == 0:
                    result.append(check)
                    done = True
                    break
            if not done:
                ok = False
#                print("fail ", i)
                break
        if ok:
            print("succes ", len(solution))
            solution.append((sol, result))
    return "\n".join([x[0] + " " + " ".join(map(str, x[1])) for x in solution])
        
inp = open("test.txt", "r")
res = open("out1.txt", "w")
cases = int(inp.readline())
lines = []
for i in range(cases):
    lines.append(map(int,inp.readline().split()))
for i in range(len(lines)):
    res.write("Case #" + str(i+1) + ":" + "\n" + findSolution(*lines[i]) + "\n")