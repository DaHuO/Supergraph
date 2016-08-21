from sets import Set 
filein = open('A-large.in', 'r')
fileout = open('A-large.out', 'w')
 
T = int(filein.readline())
for t in range(T):
    fileout.write('Case #%d: ' % (t + 1))
    base = int(filein.readline())
    
    seen = Set([])
    mark = base
    if base == 0:
        fileout.write("INSOMNIA"+'\n')
    else:
        while len(seen) < 10:
            copy = mark
            while copy > 0:
                if copy%10 not in seen:
                    seen.add(copy%10)
                copy = copy/10
            mark = mark + base

        fileout.write(str(mark-base)+'\n')
 
filein.close()
fileout.close()