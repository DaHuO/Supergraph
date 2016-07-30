import math

valid = []
first = ""


def test(C,r, p ,s):
    orig = C
    if (C.count('P') != p):
        return None
    if (C.count('R') != r):
        return None
    if (C.count('S') != s):
        return None
    while True:
        CC = ""
        for i in range(0, len(C),2):
            G = ""
            if C[i] < C[i+1]:
                G = C[i] + C[i+1]
            else:
                G = C[i+1] + C[i]
            if (G == 'PR'):
                G = 'P'
            elif (G == 'PS'):
                G = 'S'
            elif (G == 'RS'):
                G = 'R'
            else:
                print("ERROR")
            CC += G
        C = CC
        if (len(C) == 1):
            global valid
            global first
            if valid == []:
                first = orig
            valid.append(orig)
            return orig
        for i in range(0, len(C), 2):
            G = ""
            if C[i] < C[i+1]:
                G = C[i] + C[i+1]
            else:
                G = C[i+1] + C[i]
            if (G == "SS") or (G == "PP") or (G == "RR"):
                return None


games = ['PR', 'PS', 'RS'];
def generate(r, p, s, C, l):
    global games

    if (len(C) == l):
        return test(C,r, p, s)
    for x in games:
        generate(r,p,s,C + x, l)

    return None

def solve(n, r, p, s):
    global first
    global valid
    first = ""
    valid = []
    a = generate(r, p, s, '', 2 ** n)

    valid.sort()
    if (first != ""):
        if (first != valid[0]):
            print("ERROR")
    else:
        return "IMPOSSIBLE"
    return first


def output_res(caseno,output, f):
    s = "Case #{}: {}".format(caseno,output)
    print(s)#

    f.write(s + "\n")



f = open("input.txt")
f = open("A-small-attempt4.in")
outfile = open("output","w+")
T = int(f.readline())
for case in range(1, T + 1):
    n, r, p, s = map(int,f.readline().strip().split())
    output_res(case, solve(n, r, p, s),outfile)

