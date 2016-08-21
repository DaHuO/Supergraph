t = input()
ll = ['-', '+']
for inp in range(t):
    data = list(raw_input().strip())
    data.reverse()
    turns = 0
    for elem in data:
        lookfor = ll[turns%2]
        if elem == lookfor: turns += 1

    print "Case #%d: %d" % (inp+1, turns)
