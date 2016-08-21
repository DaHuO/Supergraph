# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

num_trials = int(input())

def compute():
    N = int(input())
    F = list(map(lambda x:int(x)-1,input().split()))
    #print(F)
    ty = ['u'] * N # type. possibilities are: unknown, cycle, impossible, wall, mutual friend
    le = [0] *  N # length of cycle or wall (for 'm' it's 2)
    we = [0] * N # if wall, who is at the end?

    for i in range(0, N):
        if F[F[i]] == i:
            ty[i] = 'm'
            le[i] = 2
            we[i] = F[i]

    maxCycleLength = 0

    for i in range(0, N):
        if ty[i] != 'u':
            continue
        curr = i
        chain = []
        chain.append(curr)
        completed = False
        while (not completed):
            curr = F[curr]
            if ty[curr] == 'c': # cycle
                for j in chain:
                    ty[j] = 'i' # impossible
                completed = True
            elif ty[curr] == 'w' or ty[curr] == 'm':
                l = len(chain)
                wall_length = le[curr]
                wall_end = we[curr]
                for j in range(0, l):
                    ty[chain[j]] = 'w'
                    le[chain[j]] = wall_length + l-j
                    we[chain[j]] = wall_end
                completed = True
            elif ty[curr] == 'i':
                for j in chain:
                    ty[j] = 'i' # impossible
                completed = True       
            elif curr in chain:
                currIndex = chain.index(curr)
                l = len(chain)
                cycleLength = l - currIndex
                if maxCycleLength < cycleLength:
                    maxCycleLength = cycleLength
                for j in range(currIndex, l):
                    ty[chain[j]] = 'c'
                    le[chain[j]] = cycleLength
                for j in range(0, currIndex):
                    ty[chain[j]] = 'i'
                completed = True
            else:
                chain.append(curr)

    maxWallLength = [0] * N # size of largest wall ending in i
    for i in range(0, N):
        if ty[i] == 'w' or ty[i] == 'm':
            wall_end = we[i]
            if maxWallLength[wall_end] < le[i]:
                maxWallLength[wall_end] = le[i]



    # print(ty)
    # print(le)
    # print(we)
    # print(maxWallLength)
    # print(maxCycleLength)
    combinedWalls = 0
    for i in range(0 ,N):
        if ty[i] == 'm':
            # subtract 2 to avoid double counting
            combinedWalls += maxWallLength[i] + maxWallLength[F[i]] - 2 

    combinedWalls //= 2

#    count_type_m = len([i for i in range(0, N) if ty[i] == 'm'])
    ans = max(combinedWalls, maxCycleLength)

    return str(ans)

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + compute())
