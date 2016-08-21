# Eric Lee < e@ericdlee.com >
# Google Code Jam 2015
# 
# Usage: python A.py small
# list(next()) # List of chars
# [int(n) for n in next().split()] # List of ints
# If multiline, return a list of strings. Else, return a string.

import os, sys, math, fractions

def solve_case(next):
    
    N = int(next())
    if N == 0:
        return "INSOMNIA"
    visited = set()
    num = 0
    for i in range(100):
        num += N
        visited = visited.union(set([(num // 10**j) % 10 for j in range(int(math.log10(num)) + 1)]))
        if len(visited) == 10:
            return num






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
