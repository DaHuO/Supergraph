f = open('B-large.in', 'r')
fo = open('Plarge.out', 'w')
t = int(f.readline())
for i in range(t):
    s = f.readline()
    plus = False
    neg = False
    moves = 0
    for j in s:
        if j == "+":
            plus = True
            if neg:
                moves += 1
                neg = False
        elif j == "-":
            neg = True
            if plus:
                moves += 1
                plus = False
    if neg:
        moves += 1
    fo.write("Case #%d: %d\n"%((i+1),moves))
fo.close()
f.close()
