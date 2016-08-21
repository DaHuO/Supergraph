#!/usr/bin/python
import sets
import sys

di = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]


def set_known(l1, mp, lst, num, res):
    n = 0
    if (l1 in mp and mp[l1] > 0):
        n = mp[l1]
        mp[l1] = 0
        for i in range(0, n):
            res.append(num)

	for i in range(0, len(lst)):
            mp[lst[i]] = mp[lst[i]] - n

    return n
    
def solve(lt):
    mp = {}
    nm = 0
    res = []
    for l in lt:
        if l in mp:
            mp[l] = mp[l] + 1
        else:
            mp[l] = 1
        nm = nm + 1

    set_known('X', mp, ['S', 'I'], 6, res)
    set_known('S', mp, ['E', 'V', 'E', 'N'], 7, res)

    set_known('Z', mp, ['E', 'R', 'O'], 0, res)
    set_known('U', mp, ['F', 'O', 'R'], 4, res)
    set_known('W', mp, ['T', 'O'], 2, res)
   
    set_known('G', mp, ['E', 'I', 'H', 'T'], 8, res)
    set_known('H', mp, ['T', 'R', 'E', 'E'], 3, res)
    set_known('O', mp, ['E', 'N'], 1, res)
  
    set_known('F', mp, ['I', 'V', 'E'], 5, res)
    set_known('I', mp, ['N', 'N', 'E'], 9, res)

    res.sort()
    return res
   
            

f = open(sys.argv[1], 'r')
N = int(f.readline())
for i in range(0, N):
    letter = f.readline().strip()
    r = solve(letter)
    s = ""
    for n in r:
        s += str(n)
    print "Case #"+str(i+1)+": " + s


