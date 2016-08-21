def changes(ps):
    ch = 0
    currStream = ps[0]
    for p in ps:
        if p != currStream:
            ch += 1
            currStream = p 
    return ch

t = int(raw_input())
for case in range(1, t+1):
    pan = str(raw_input())
    result = changes(pan)
    if pan.endswith("-"):
        result += 1
    print "Case #%d: %d" % (case, result)
