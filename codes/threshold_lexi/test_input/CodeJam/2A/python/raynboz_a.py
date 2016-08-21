import numpy as np
from itertools import permutations

fin = open('ain.txt', 'r')
fout = open('aout.txt', 'w')

T = int(fin.readline())

def valid(i):
    if len(i) == 1:
        return True
    x = []
    for j in range(len(i) // 2):
        if i[2*j] == i[2*j+1]:
            return False
        if i[2*j] == "R" and i[2*j+1] == "P":
            x += ["P"]
        elif i[2*j] == "R" and i[2*j+1] == "S":
            x += ["R"]
        elif i[2*j] == "P" and i[2*j+1] == "R":
            x += ["P"]
        elif i[2*j] == "P" and i[2*j+1] == "S":
            x += ["S"]
        elif i[2*j] == "S" and i[2*j+1] == "R":
            x += ["R"]
        elif i[2*j] == "S" and i[2*j+1] == "P":
            x += ["S"]
    return valid(x)


def solve():
    N, R, P, S = tuple([int(i) for i in fin.readline().split()])
    
    x = permutations("P"*P + "R"*R + "S"*S)
    for i in x:
        if valid(list(i)):
            return ''.join(i)

    return "IMPOSSIBLE"

for i in range(T):
    fout.write("Case #" + str(i+1) + ": " + str(solve()) + "\n")

fin.close()
fout.close()
