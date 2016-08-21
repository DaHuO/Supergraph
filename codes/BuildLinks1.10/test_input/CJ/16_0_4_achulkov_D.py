__author__ = 'Andrey'
import sys

fin = open("D-small-attempt0.in", "r")
fout = open("output.txt", "w")
t = int(fin.readline().rstrip())
for i in range(1, t + 1):
    k, c, s = map(int, fin.readline().rstrip().split())
    print("Case #" + str(i) + ":", *[j for j in range(1, s + 1)], sep=" ", file=fout)