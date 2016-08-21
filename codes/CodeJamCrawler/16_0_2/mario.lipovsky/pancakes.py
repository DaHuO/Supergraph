from itertools import groupby

T = int(input())

def solve():
    seq = [k for k, g in groupby(input())]
    return len(seq) - int(seq[-1] == '+')

for t in range(T):
    print("Case #{}: {}".format(t+1, solve()))
