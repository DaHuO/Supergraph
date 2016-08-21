#!/usr/bin/python
def Problem_A(N):
    for i in range(1, N+1):
        numbre = int(input())
        l = []
        done = False
        test = 0
        for j in range(1, N+1):
            test = j * numbre
            for k in str(test):
                if not k in l:
                    l.append(k)
            if len(l) == 10:
                done = True
                break
        if done:
            print('Case #{}: {}'.format(i,test))
        else:
            print('Case #{}: INSOMNIA'.format(i))

N = int(input())
Problem_A(N)