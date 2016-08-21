# Eric Lee < e@ericdlee.com >
# Google Code Jam 2015
# 
# Usage: python A.py small
# list(next()) # List of chars
# [int(n) for n in next().split()] # List of ints
# If multiline, return a list of strings. Else, return a string.

import os, sys, math, fractions

def solve_case(next):
    
    K, C, S = [int(n) for n in next().split()]
    needed = math.ceil(K / C)
    if needed > S:
        return "IMPOSSIBLE"
    ret = []
    for i in range(needed):
        s = 0
        for j in range(C):
            s = (s * K) + min(i * C + j, K - 1)
        ret.append(str(s + 1))
    return " ".join(ret)






# ---------------------------------------------------------------------------- #

def solve(next, emit):
    cases = int(next())
    for case in range(1, cases + 1):
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
