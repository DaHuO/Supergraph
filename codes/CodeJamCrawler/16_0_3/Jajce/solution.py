from math import sqrt
from itertools import count, islice
import time
import sys


def is_dividable(n, m):
    if not n % m:
        return m
    return False

def isjam(str):
    n = 2
    answer = str
    num = ""
    arr = [3, 2, 3, 2, 7, 2, 3, 2, 3]
    while n != 11:
        curnum = int(str, n)
        pr = is_dividable(curnum, arr[n - 2])
        if pr:
            answer += (" %d" % pr)
            num += "%d " % curnum
        else:
            return False
        n += 1
    print(answer, num)
    return answer

f = open("input.txt", 'r')
ff = open("ans.txt", 'w')
doesntmatter = int(f.readline())
inputc = [int(x) for x in f.readline().split()]
jamsize = inputc[0]
amm = inputc[1]
start_time = time.time()
counter = 0
ff.write("Case #1:\n")
fnumberstr = "1%s1" % ("0"*(jamsize-2))
curnum = int(fnumberstr, 2)
while counter != amm:
    answer = isjam("{0:b}".format(curnum))
    if answer:
        counter += 1
        ff.write("%s\n" % answer)
    curnum += 2
ff.close()
f.close()
print("--- %s seconds ---" % (time.time() - start_time))
