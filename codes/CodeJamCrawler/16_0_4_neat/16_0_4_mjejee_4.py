size = int (raw_input())


def processfractal(k, c, s):
    # k = number of tiles
    # c = complexity
    # s = max known tiles

    # s = k
    newperold = k ** (c-1) #old tile length in new tiles

    discover = []
    for i in range (k):
        discover.append (str(i*newperold+1))
    return ' '.join(discover)

i=0

while True:
    if i>=size:
        break
    i = i+1
    linearray = raw_input().split(' ')
    print 'Case #'+ str(i) + ': ' + processfractal(int(linearray[0]),int(linearray[1]), int(linearray[2]))