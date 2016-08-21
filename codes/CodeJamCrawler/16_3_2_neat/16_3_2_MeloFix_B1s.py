T = int(input())

for LoopC in range(1,T+1):
    B, M = map(int,input().split())
    ret = 'IMPOSSIBLE'

    Map = []

    if ret == 'IMPOSSIBLE':

        for x in range(B):
            Map.append([0]*(B-1) + [1])
        Map[0] = [0]+[1]*(B-1)
        Map[-1] = [0]*B
        
        for N in range(int(2**((B-1)*(B)/2))):
            N = (bin(N)[2:]).format()
            n = []
            n += N
            N = n
            while len(N)<(B-1)*B/2:
                N.insert(0,'0')
            
            N.reverse()
            
#            print(N)
            
            Min = [0]*B
            Min[-1] = 1

            for x in range(0,B):
                for y in range(x+1,B):
                    Map[x][y] = int(N.pop(0))

            for x in range(B-1,-1,-1):
                for y in range(x+1,B):
                    if Map[x][y] == 1:
                        Min[x] += Min[y]

            if Min[0] == M and Map[0][B-1]==1:
                ret = "POSSIBLE"
                break

    print("Case #{}: {}".format(LoopC,ret))
    if ret == "POSSIBLE":
        for x in Map:
            for y in x:
                print(y,end='')
            print()
