#!/usr/bin/env python



def read():
    return map(int, raw_input().split())


def work(cases, (nInit, nRep, nChoose)):
    nRep -= 1
    
    if nRep == 0:
        if nChoose == nInit:
            print "Case #%d:" % cases,
            print " ".join(map(str, range(1, nInit + 1)))
        else:
            print "Case #%d: IMPOSSIBLE" % cases
        return
    
    elif nChoose < nInit - 1:
        print "Case #%d: IMPOSSIBLE" % cases
        return

    elif nInit == 1:
        print "Case #%d: 1" % cases
        return
    
    ans = []
    for i in range(1, nInit):
        ans.append((nInit ** nRep) * i + 1)

    print "Case #%d:" % cases,
    print " ".join(map(str, ans))


if __name__ == "__main__":
    for i in range(int(raw_input())):
        work(i + 1, read())
