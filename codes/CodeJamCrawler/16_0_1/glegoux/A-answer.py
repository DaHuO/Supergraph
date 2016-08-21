#!/usr/bin/env python3

def sleep(N):
    if N == 0:
        return "INSOMNIA"
    i = 1
    d = dict()
    while len(d) != 10:
        n = i*N
        for s in str(n):
            d[s] = True
        i = i + 1
    return n


def print_answer(n, result):
    res = ""
    if type(result) in [list, tuple]:
        res = " ".join(map(str, result))
    elif type(result) == int:
        res = str(result)
    elif type(result) == str:
        res = result
    print("Case #{}: {}".format(n, res))

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        print_answer(t + 1, sleep(N))

if __name__ == "__main__":
    main()
