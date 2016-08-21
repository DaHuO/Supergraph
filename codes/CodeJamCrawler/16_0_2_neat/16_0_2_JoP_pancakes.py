import sys

def flip(inp):
    inp = list(inp)
    for i in range(0,len(inp)/2):
        inp[-i-1] = "+" if inp[-i-1] == "-" else "-"
        inp[i] = "+" if inp[i] == "-" else "-"
    if len(inp) % 2 == 1:
        m = len(inp)/2
        inp[m] = "+" if inp[m] == "-" else "-"
    return ''.join(inp)

def solve(inp):
    if len(inp) == 0:
        return 0

    if inp[-1] == "+":
        return solve(inp[0:-1])

    if len(inp) == 1:
        return 1 # must be -

    if inp[0] != inp[-1]:
        return 1 + solve(flip(inp))
    else:
        return 1 + solve(flip(inp[::-1]))

    return -1

inp = sys.stdin.read().splitlines()
T = int(inp[0])
for t in range(0,T):
    print("Case #%d: %d" % (t+1, solve(inp[t+1])))
