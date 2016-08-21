import sys

import sys
data = [v.rstrip() for v in open(sys.argv[1])]
T = data[0]
dataset = data[1:]

def ToRoom(line):
    rs = [int(v) for v in line.split()]
    result = []
    sum = 0
    for i, r in enumerate(rs):
        sum += r
        result.append([chr(ord('A')+i), r])
    return result, sum

def GetTwoRoom(rooms, sum):
    def popRoom(rs):
        if len(rs) == 0:
            return "", rs
        r = rs[0][0]
        rs[0][1] -= 1
        if rs[0][1] == 0:
            rs.pop(0)
        return r, sorted(rs, key=lambda v: v[1], reverse=True)
    result = ""
    r, rs = popRoom(rooms)
    result += r
    if len(rs) == 2 and rs[0][1] == 1:
        return result, rs
    r, rs = popRoom(rs)
    result += r
    return result, rs

def solv(rooms, sum):
    rooms = sorted(rooms, key=lambda v: v[1], reverse=True)
#    print(rooms)
    result = []
    while True:
        if len(rooms) == 0:
            return result
        r, rs = GetTwoRoom(rooms, sum)
        result.append(r)
        rooms = rs
    return result

for i in range(int(T)):
    N = dataset.pop(0)
    rooms, sum = ToRoom(dataset.pop(0))
    result = solv(rooms, sum)
    print("Case #{0}: {1}".format(i+1, ' '.join(result)))
