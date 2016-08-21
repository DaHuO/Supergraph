#!/usr/bin/env python


def read():
    return input()


def work(cases, N):
    
    if N == 0:
        print "Case #%d: INSOMNIA" % cases
        return

    avail = [False for i in range(10)]

    cur = N
    while True:
        for digit in map(int, str(cur)):
            avail[digit] = True
        
        if all(avail):
            break
        
        cur += N
    
    print "Case #%d: %d" % (cases, cur)
    

if __name__ == "__main__":
    for i in range(int(raw_input())):
        work(i + 1, read())
