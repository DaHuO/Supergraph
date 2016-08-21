import sys, math

T = int(input())
for i in range(T):
    N = input()
    N_3 = int(N)
    l_init = [-1] * 10
    count = 0
    if N_3 == 0:
        print('Case #'+str(i+1)+': INSOMNIA')
    else:
        while l_init[0] == -1 or l_init[1] == -1 or l_init[2] == -1 or l_init[3] == -1 or l_init[4] == -1 or l_init[5] == -1 or l_init[6] == -1 or l_init[7] == -1 or l_init[8] == -1 or l_init[9] == -1:
            count += 1
            N_2 = N * count
            l_transit = map(int, list(str(N_2)))
            for j in range(len(l_transit)):
                l_init[l_transit[j]] = 0
        print('Case #'+str(i+1)+': '+str(N_2))