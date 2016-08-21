__author__ = 'Andrey'
import sys

seen = [False for i in range(10)]


def solve(n):
    if n == 0:
        return "INSOMNIA\n"
    for q in range(10):
        seen[q] = False
    s = 0
    curr = n
    while s != 10:
        for char in str(curr):
            c = int(char)
            if not seen[c]:
                #print(c)
                seen[c] = True
                s += 1
        if s == 10:
            break
        curr += n
    return str(curr) + "\n"


fin = open("A-large.in", "r")
fout = open("output.txt", "w")
t = int(fin.readline().rstrip())
for i in range(t):
    fout.write("Case #" + str(i + 1) + ": " + solve(int(fin.readline().rstrip())))
