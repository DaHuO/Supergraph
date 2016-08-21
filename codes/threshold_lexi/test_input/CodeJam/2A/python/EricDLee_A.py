# Eric Lee < e@ericdlee.com >
# Google Code Jam 2016
# 
# Usage: python A.py small
# list(next()) # List of chars
# [int(n) for n in next().split()] # List of ints
# If multiline, return a list of strings. Else, return a string.

import os, sys, math, fractions

t = {
    "P": "PR",
    "R": "RS",
    "S": "PS"
}

def s(N, R, P, S):
    if N == 0:
        if P > 0:
            return "P"
        elif R > 0:
            return "R"
        else:
            return "S"
    pr = (P + R - S) / 2
    ps = (P + S - R) / 2
    rs = (R + S - P) / 2
    if pr < 0 or ps < 0 or rs < 0:
        return False
    last = s(N - 1, rs, pr, ps)
    if not last:
        return False
    return "".join([t[x] for x in last])
    

def solve_case(next):
    
    N, R, P, S = [int(n) for n in next().split()]
    ret = s(N, R, P, S)
    if not ret:
        return "IMPOSSIBLE"
    for n in range(1, N):
        i = 2 ** n
        j = 2 ** (N - n - 1)
        b = ""
        for k in range(j):
            step = (2**N)*k/j
            b += "".join(sorted([ret[step : step + i], ret[step + i : step + 2*i]]))
        ret = b
    return ret






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
