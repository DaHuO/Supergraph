'''
1
1
10


1
2
10 20
20 40
10 30



1
2
1 2
2 3
1 2

1
2
1 2
1 2
2 3



1
3
1 2 3
2 3 5
3 5 6
2 3 4
1 2 3
'''
from math import *

def rl(l): return range(len(l))



f = open("b3.out", mode='w')

T = int(input())
N = 0


v = []




def do(rinds):

    #print("entering do, rinds =", rinds)
    
    # check if past the end
    if len(rinds) == N+1:
        return None

    
    p = len(rinds)
    mat = [v[i] for i in rinds]
    

    if len(rinds) == N: # ideally this would be combined with down below
        usedinds = set()
        for rind in rinds:
            usedinds.add(rind)

        missingcolind = -1
        for col in range(N):
            worked = False
            for sheetind in range(len(v)): # simple search SPEED   # something up with same?  in 1 2 \ 2 3
                sheet = v[sheetind]
                if not sheetind in usedinds:
                    #print("condsidering sheetind", sheetind, "col", col)
                    if sheet == [mat[i][col] for i in range(N)]: # not v[i][col] - mistake
                        worked = True
                        usedinds.add(sheetind)
                    
                    #print(sheet, [mat[i][col] for i in range(N)])
                        
            if not worked:
                if missingcolind != -1: # second bad column?
                    #print("missingcolind already", missingcolind, ", also", col)
                    return None
                else:
                    missingcolind = col

        return [mat[i][missingcolind] for i in range(N)]
            
    

    ans = None



    # check if we should proceed with the columns
    
    # get all column parts from the matrix

    numbad = 0
    for ci in range(N):
        try:
            colpart = [mat[i][ci] for i in range(p)]
        except:
            print(mat, i, ci, p)


        # simple test if this starts a column, ignoring repeats. TIMING
        # we need to allow one to fail
        good = False
        for vi in range(len(v)):
            if vi not in rinds:
                if v[vi][:len(colpart)] == colpart:
                    good = True

        if not good:
            numbad += 1
            # TIMING early break

    if numbad > 1:
        #print("numbad", numbad)
        return None



    # check if we can proceed with the column ordering constraint.  First add valid indexes...

    for nextri in range(len(v)):
        if nextri not in rinds:
            newrinds = [e for e in rinds]
            newrinds.append(nextri)
            # then generate matrix...

            mat = [v[i] for i in newrinds]

            # then check.

            good = True
            for col in range(len(mat[0])):
                if not all(mat[i][col] > mat[i-1][col] for i in range(1, len(mat))): # strictly greater # forgot I knew this
                    good = False


            # decide whether to proceed
            if good:
                ans = do(newrinds) # recursion point  # why 3-quote comment not work? oh yeah same line.

                if ans:
                    return ans
            else:
                #print("Not continuing with newrinds", newrinds)
                '''print(">")
                print(mat)'''
            
    

for nt in range(1, T+1):
    N = int(input())
    v = [] # initialize!

    
    for i in range(2*N-1):
        cline = list(map(int, input().split()))
        v.append(cline)

    ans = None

    try:
        assert len(v) == 2*N - 1
    except:
        print(v)
        print(len(v), 2**N - 1)
        print("ERROR")
        assert False

    for i in range(2*N-1):
        l = [i]
        
        tans = do(l)
        if tans:
            ans = tans
            break
        
    print(ans)
    ans = " ".join(str(e) for e in ans)
    towrite = "Case #"+str(nt)+": "+str(ans)+'\n'
    f.write(towrite)
    print(towrite, end="")
    
f.close()

# note it can always be a missing column - symmetry

'''
1
1
10


1
2
10 20
20 40
10 30



1
2
1 2
2 3
1 2

1
2
1 2
1 2
2 3



1
3
1 2 3
2 3 5
3 5 6
2 3 4
1 2 3
'''
