f = open('A-large.in', 'r')
fout = open('out.txt', 'w')

T = int(f.readline())

for t in range(T):
    N = int(f.readline())

    if N == 0:
        fout.write("Case #%d: INSOMNIA\n" % (t+1))
        continue
    
    seen = [0]*10

    i = 1
    while 1:
        current = N*i
        currentS = str(current)
        for j in range(len(currentS)):
            seen[int(currentS[j])] = 1

        allDone = True
        for j in range(10):
            if not seen[j]:
               allDone = False
               break

        if allDone:
            fout.write("Case #%d: %d\n" % (t+1, current))
            break

        i += 1

f.close()
fout.close()
