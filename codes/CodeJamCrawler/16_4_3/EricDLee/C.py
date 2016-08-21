# Eric Lee < e@ericdlee.com >
# Google Code Jam 2016
# 
# Usage: python A.py small
# list(next()) # List of chars
# [int(n) for n in next().split()] # List of ints
# If multiline, return a list of strings. Else, return a string.


#  1
# 4 2
#  3

import os, sys, math, fractions


def nxt(pos):
    row, col, dir = pos
    if dir == 1:
        return (row - 1, col)
    elif dir == 2:
        return (row, col + 1)
    elif dir == 3:
        return (row + 1, col)
    else:
        return (row, col - 1)

def solve_case(next):
    
    R, C = [int(n) for n in next().split()]
    p = [int(n) for n in next().split()]
    N = len(p)
    P = []
    for i in range(N / 2):
        x, y = p[2*i], p[2*i+1]
        d1, d2 = (x - y) % N, (y - x) % N
        if min(d1, d2) % 2 != 1:
            return ["IMPOSSIBLE"]
        if d1 < d2:
            P.append((y, x, d1))
        else:
            P.append((x, y, d2))
    P = sorted(P, key=lambda t: t[2])
    print(P)
    hedges = [["?" for _ in range(C)] for _ in range(R)]
    for pair in P:
        a, b, dist = pair
        print("pair", a, b)
        pos, goal = None, None # (row, col, dir)
        if a <= C:
            pos = (-1, a - 1, 3)
        elif a <= C + R:
            pos = (a - C - 1, C, 4)
        elif a <= 2*C + R:
            pos = (R, 2 * C + R - a, 1)
        else:
            pos = (N - a, -1, 2)
        start = None
        
        if b <= C:
            goal = (-1, b - 1)
        elif b <= C + R:
            goal = (b - C - 1, C)
        elif b <= 2*C + R:
            goal = (R, 2 * C + R - b)
        else:
            goal = (N - b, -1)
        
        while (pos[0], pos[1]) != goal:
            print("pos", pos[0], pos[1], pos[2])
            if start != None and (pos[0] < 0 or pos[1] < 0 or pos[0] >= R or pos[1] >= C):
                print str(hedges)
                return ["IMPOSSIBLE"]
            nextR, nextC = nxt(pos)
            newDir = None
            if nextR < 0 or nextC < 0 or nextR >= R or nextC >= C:
                pass
            else:
                if hedges[nextR][nextC] == "?":
                    if pos[2] == 1 or pos[2] == 3:
                        hedges[nextR][nextC] = "\\"
                    else:
                        hedges[nextR][nextC] = "/"
                if hedges[nextR][nextC] == "\\":
                    if pos[2] == 1:
                        newDir = 4
                    elif pos[2] == 2:
                        newDir = 3
                    elif pos[2] == 3:
                        newDir = 2
                    else:
                        newDir = 1
                else:
                    if pos[2] == 1:
                        newDir = 2
                    elif pos[2] == 2:
                        newDir = 1
                    elif pos[2] == 3:
                        newDir = 4
                    else:
                        newDir = 3
            pos = (nextR, nextC, newDir)
            if start == None:
                start = (nextR, nextC)
            elif nextR == start[0] and nextC == start[1]:
                print str(hedges)
                return ["IMPOSSIBLE"]
    return ["".join(x).replace("?", "/") for x in hedges]






# ---------------------------------------------------------------------------- #

def solve(next, emit):
    cases = int(next())
    for case in range(1, cases + 1):
        print("CASE", case)
        sol = solve_case(next)
        if isinstance(sol, list):
            emit("Case #{0}:".format(case))
            for line in sol:
                emit(str(line))
        else:
            emit("Case #{0}: {1}".format(case, str(sol)))
        print("{0} / {1}".format(case, cases))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python {0} small".format(sys.argv[0]))
        exit()
    prefix = sys.argv[0][:-3] + "-" + sys.argv[1]
    suffix = ".in"
    for file in os.listdir(os.path.dirname(os.path.realpath(__file__))):
        if file.startswith(prefix) and file.endswith(suffix):
            print("Loading " + file)
            file_in = open(file, "r")
            file_out = open(file[:-3] + ".out", "w")
            solve(lambda: file_in.readline().strip(), lambda x: file_out.write(str(x) + "\n"))
            file_in.close()
            file_out.close()
            print("Complete.")
