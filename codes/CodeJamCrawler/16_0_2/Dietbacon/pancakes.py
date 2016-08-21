n = int(raw_input())
for k in range (0,n):
    pile = raw_input()
    flips = 0
    mode = 0
    for i in range (len(pile) - 1, -1, -1):
        if (pile[i] == '-' and mode == 0):
            flips += 1
            mode = 1
        elif (pile[i] == '+' and mode == 1):
            flips += 1
            mode = 0
    print 'Case #' + str(k+1) + ': ' + str(flips)
