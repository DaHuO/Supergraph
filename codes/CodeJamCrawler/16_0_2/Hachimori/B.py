#!/usr/bin/env python


def read():
    return [ch == '+' for ch in raw_input()]


def swap(idx, isOk):
    swapped = [not ok for ok in isOk[:idx+1]]
    swapped.reverse()
    isOk = swapped + isOk[idx+1:]
    return isOk
    
    
def calc(isOk):
    cnt = 0
    
    for idx in range(len(isOk) - 1, -1, -1):
        if isOk[idx]:
            continue
        
        if not isOk[0]:
            isOk = swap(idx, isOk)
            cnt += 1
            continue

        swappos = idx
        while swappos >= 1 and not isOk[swappos]:
            swappos -= 1

        isOk = swap(swappos, isOk)
        isOk = swap(idx, isOk)
        cnt += 2

    return cnt    
    

def work(cases, isOk):
    print "Case #%d: %d" % (cases, calc(isOk))


if __name__ == "__main__":
    for i in range(int(raw_input())):
        work(i + 1, read())
