#!/usr/bin/python3

def codejammer():
    Rounds = int(input())
    for r in range(1, Rounds + 1):
        K, C, S = [int(x) for x in input().split()]
        print("Case #{}: {}".format(r, " ".join([str(x) for x in range(1, K+1)])))

if __name__ == '__main__':
    codejammer()

