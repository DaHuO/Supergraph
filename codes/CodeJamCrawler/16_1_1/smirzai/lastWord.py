__author__ = 'smirzai'
import fileinput

inputFile = fileinput.input();

#inputFile = f = open('sample.txt', 'r')


def solve(s):
    if s[-1] == '\n':
      s = s[:-1]
    r = s[0]
    for ch in s[1:]:
        if ch >= r[0]:
            r = ch + r
        else:
            r = r + ch
    return r


t = int(inputFile.readline())
for i in range(t):
    st = inputFile.readline()
    print("Case #" + str(i+1) + ": " + solve(st))
