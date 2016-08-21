def getBottom(n):
    index = None
    for i,pan in enumerate(n[::-1]):
        if pan == '-':
            index = len(n)-1-i
            break
    
    return index

def flip(n,index):
    for i,x in enumerate(n[:index+1]):
        if x == '-':
            n[i] = '+'
        else:
            n[i] = '-'

def find(n,case):
    index = getBottom(n)
    if index is None:
        print "Case #"+str(case)+": 0"
        return
    moves = 0
    while index is not None:
        flip(n,index)
        index=getBottom(n)
        moves = moves + 1

    print "Case #"+str(case)+": " + str(moves)

f = open('workfile', 'r')
for i,line in enumerate(f):
    if i != 0:
        find(list(line.strip()),i)

