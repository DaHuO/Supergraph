



def findLastMinus(pList):
    pLen = len(pList)
    for i in range(pLen-1, -1, -1):
        if pList[i] == '-':
            return i
    return None

def flipChar(c):
    if c == '+':
        return '-'
    elif c == '-':
        return '+'
    else:
        print 'ERROR'

def findNumFlips(pList):
    lastMinus = findLastMinus(pList)
    if lastMinus == None:
        return 0
    else:
        flippedList = [flipChar(c) for c in pList[:lastMinus+1]]
        return 1 + findNumFlips(flippedList)


def main():
    T = int(raw_input())
    for i in range(1,T+1):
        panString = raw_input()
        ans = findNumFlips(list(panString))
        print "Case #{}: {}".format(i, ans)

if __name__ == "__main__":
    main()