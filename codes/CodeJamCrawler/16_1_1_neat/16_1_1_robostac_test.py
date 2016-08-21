import math

def test(a,b):
    if b == "":
        return a
    elif b[0] >= a[0]:
        return test(b[:1] + a , b[1:])
    return test(a + b[:1], b[1:])

def solve(N):
    return test(N[:1],N[1:])


def output_res(caseno,output, f):
    s = "Case #{}: {}".format(caseno,output)
    print(s)
    f.write(s + "\n")
import sys
sys.setrecursionlimit(1500)

f = open("input.txt")
f = open("A-small-attempt0.in")
f = open("A-large.in")
outfile = open("output","w+")
T = int(f.readline())
for case in range(1, T + 1):
    N = f.readline().strip()
    output_res(case, solve(N),outfile)

