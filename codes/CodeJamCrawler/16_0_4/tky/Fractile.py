# Google code jam fractal tiling

def masterTile(K,C,k):
    # returns the position of the direct descendent for a particular subgraph
    if k > K:
        return(-1)
    else:
        out = k
        for c in range(C-1,0,-1):
            out = out + (k-1)*(K**c)
        return(out)
       
T = int(input()) # read number of cases from stdin

for j in range(1,T+1):

    K, C, S = [int(s) for s in input().split(" ")] # read input string (python3)

    # catch trivial cases (final pattern is base pattern)
    if (C == 1)|(K == 1):
        # need to check all tiles to certainly get an answer
        if (S < K):
            print("Case #{}: {}".format(j,"IMPOSSIBLE")) # case result output
        else:
            outstring = ''
            for i in range(1,K+1):
                outstring = outstring + " {}".format(i)
            print("Case #{}:{}".format(j,outstring)) # case result output
    elif (S >= K):
        # shortcut: can just check the first tiles
        outstring = ''
        for i in range(1,K+1):
            outstring = outstring + " {}".format(i)
        print("Case #{}:{}".format(j,outstring)) # case result output
    else:
        # choosing the right tiles, a minimum of ceil(K/2) is needed
        if (S < K/2):
            print("Case #{}: {}".format(j,"IMPOSSIBLE")) # case result output
        else:
            # one tile can maximally give answer for two base tiles
            # chose tiles right of direct descendants for information about
            # this subgraph and the one to the right
            i = 1
            tile = [2] # 2 is right of direct descendant from first bas tile
            while (i < K/2):
                nexttile = masterTile(K,C,2*i+1) + 1
                if nexttile > K**C: # only need to probe the last subgraph
                    nexttile = K**C
                tile = tile + [nexttile]
                i += 1
            
            outstring = ''
            for i in range(0,len(tile)):
                outstring = outstring + " {}".format(tile[i])
            print("Case #{}:{}".format(j,outstring)) # case result output
            
