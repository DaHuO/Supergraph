from math import *

def rl(l): return range(len(l))



f = open("c2.out", mode='w')

T = int(input())
F = []


# we will not require the first person, l[0], to be next to bff until final check since could wrap around.  so do() starts with lists of len 1.



def do(l):

    #print("entering do", l)
    
    ans = 0

    # works if we stop here?
    for d in range(1):

        good = False


        # check if person 0 next to bff

        f0 = F[l[0]]
        #[F[l[-1]], F[l[1]]]:

        f_1 = F[l[-1]]
        if f_1 in [l[-2], l[0]] and f0 in [l[-1], l[1]]:
            good = True

        if good:
            ans = len(l)

        #print("loop checked, ans set to", ans)
    

    # find the next bff
    nextr = F[l[-1]]

    # if they're already together:
    if len(l) >= 2 and nextr == l[-2]:

        # then the RHS of the list is a loose constraint.  We can sit anyone here.
        # We might end up satisfying this again, which will be checked in recursion

        sl = set(l)

        for kid in range(N): # kid ID
            if not kid in sl:

                newl = [e for e in l]
                newl.append(kid)
                ans = max(do(newl), ans) # assign it
                ''' recursive entry point '''
                


    else:
        # binding constraint

        if not nextr in l:
            
            newl = [e for e in l]
            newl.append(nextr)
            #print("continuing with newl", newl)
            ans = max(do (newl), ans)
            ''' recursive entry point '''
        '''
        else: # we are stuck
            #print("we are stuck ",end='')
            #if l[0] == nextr:
            newl = l
            if F[newl[-1]] in [newl[-2], newl[0]] and F[newl[0]] in [newl[1], newl[-1]]: # end conditions of friends
                ans = max(ans, len(newl))
            else:
                ans = max(ans, 0)
            #print(ans)
        '''

    return ans


for nt in range(1, T+1):
    N = int(input())
    F = []
    
    '''v = []
    for i in range(N):
        cline = list(map(int, input().split()))
        if len(cline) == 1: cline = cline[0]
        v.append(cline)
    '''
    v = list(map(int, input().split()))
    for i in range(len(v)):
        v[i] = v[i] - 1 # normalize to 0-index

    F = v # assignment#######


    ans = 0

    

    if len(F) == 1:
        ans = 1

    else:

        for a in range(N):
            for b in range(N):
                if a == b: continue

                ans = max(ans, do([a, b]))

    
    towrite = "Case #"+str(nt)+": "+str(ans)+'\n'
    f.write(towrite)
    print(towrite, end="")
    
f.close()
