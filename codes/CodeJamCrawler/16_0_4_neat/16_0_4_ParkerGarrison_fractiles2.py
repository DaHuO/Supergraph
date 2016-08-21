from math import *

def rl(l): return range(len(l))

'''
8
2 3 2
1 1 1
2 1 1
2 1 2
3 2 3
3 4 3
1 18 1
17 1 17
'''


f = open("fractiles-large.out", mode='w')

T = int(input())

for nt in range(1, T+1):
    K, C, S= list(map(int, input().split()))
    #print(K, C, S)
    

    ans = ""

    # case #25 and #49, #61, #64, #96, #73

    # K is base, C is exponent

    # C is the depth
    # K is the width


    # assert that K / C >= S

    # we need to guess ceil (K / C) numbers

    if S < ceil (K / C):
        ans = "IMPOSSIBLE"

    else: 
        nums = []

        for i in range(min(ceil(K/C),S)):

            num = 1 # 1-indexed

            for dep in range(C):
                dnum = C*i+dep #min(C*i+dep, ceil(K/C))
                if dnum >= K:
                    dnum = K -1
                '''if dnum > ceil(K/C):
                    dnum = ceil(K/C)'''
                #print(dnum, K**dep)
                num += dnum * K**dep

            #if K == 1 : num = 1
            # SHouldn't need this!

            try:
                assert num <= K ** C
            except:
                print("#",nt," ",K,C,S," ", num, nums, i,dep)
            
            nums.append(num)


        ans = " ".join(str(nu) for nu in nums)
    
    towrite = "Case #"+str(nt)+": "+str(ans)+'\n'
    f.write(towrite)
    print(towrite, end="")
    
f.close()
