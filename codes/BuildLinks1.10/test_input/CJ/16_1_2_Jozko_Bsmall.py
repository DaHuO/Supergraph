import sys
import numpy as np
T = int(sys.stdin.readline())
for case in range(1, T+1):
    sys.stdout.write("Case #%d: " % case)
    
    N = int(sys.stdin.readline())
    lines = []
    for _ in range(2*N-1):
        lines.append(map(int,sys.stdin.readline().strip().split()))
    if N == 1:
        sys.stdout.write("%s\n" % ' '.join(map(str, lines[0])))
        continue
    grid = []
    missingCol = None
    for i in range(N):   
        lines = sorted(lines, key=lambda x: x[i])
        if len(lines) == 1 or (lines[0][i] != lines[1][i]):
            assert missingCol == None
            missingCol = i
            grid.append((lines[0], None))
            lines = lines[1:]
        else:
            grid.append((lines[0], lines[1]))
            lines = lines[2:]
    fillgrid = np.zeros(shape=(N,N), dtype=int)
    #firstLine = map(int, grid[0][0].split())
    #fillgrid[0] = firstLine
    grid = list(enumerate(grid))
    #print grid
    missingLine = grid[missingCol][1][0]
    fillgrid[missingCol] = missingLine
    found = [missingCol]
    while len(found) != N:
        notFound = True
        for i, (l1, l2) in grid:
            if i != missingCol and i not in found:
                l1 = np.array(l1)
                l2 = np.array(l2)
                #print l1, l2
                #print (l1[found] == fillgrid[found, i]), l2[found] != fillgrid[found, i]
                if (all(l1[found] == fillgrid[found, i]) and any(l2[found] != fillgrid[found, i])) or all(l1==l2): 
                    fillgrid[i] = l2
                    fillgrid[:, i] = l1
                    found.append(i)
                    found = sorted(found)
                    notFound = False
                    break
                    
                elif any(l1[found] != fillgrid[found, i]) and all(l2[found] == fillgrid[found, i]):
                    fillgrid[i] = l1
                    fillgrid[:, i] = l2
                    found.append(i)
                    found = sorted(found)
                    notFound = False
                    break
        #print fillgrid, found
                    
        assert not notFound,  (fillgrid, found, missingCol, grid)
#        if notFound:
#            fillgrid[missingCol] = missingLine
#            found.append(missing
#            # try filling missing
    answer = fillgrid[:, missingCol]
    sys.stdout.write("%s\n" % ' '.join(map(str, answer)))




            
            
            



