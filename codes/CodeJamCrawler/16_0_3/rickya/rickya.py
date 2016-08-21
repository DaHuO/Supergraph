from math import*
from sys import exit

t = ""
ans = []
k = 0
fout = open("output.txt", "w")
nn = 0

def ok(x):
    cur = 2
    while cur * cur <= x:
        if x % cur == 0:
            return 0
        cur += 1
        if cur > 1e4:
            break
    return 1

def fs(x):
    cur = 2
    while cur * cur <= x:
        if x % cur == 0:
            return cur
        cur += 1

def check():
    global ans
    global k
    global fout
    if int(t, 10) <= 1:
        return
    for i in range(2, 10 + 1):
        if ok(int(t, i)):
            return
    k -= 1
    ans += [t]
    if k == 0:
        for it in ans:
            print(it, end = " ", file = fout)
            for i in range(2, 10 + 1):
                print(fs(int(it, i)), end = " ", file = fout)
            print(file = fout)
        exit(0)
    print(k, "more")

def gen(n):
    global t
    if n == 0:
        check()
        return
    if n == nn or n == 1:
        t += str(1)
        gen(n - 1)
        t = t[:-1:]
        return
    for i in range(2):
        t += str(i)
        gen(n - 1)
        t = t[:-1:]

def solve(s):
    global k
    global nn
    (n, k) = map(int, s.split())
    nn = n
    gen(n)

def main():
    fin = open("input.txt", "r")
    n = int(fin.readline())
    solve(fin.readline())
    #for i in range(1, n + 1):
    #    print("Case #" + str(i) + ": " + solve(fin.readline()), file = fout)
    fin.close()
    fout.close()

if __name__ == "__main__":
    main()