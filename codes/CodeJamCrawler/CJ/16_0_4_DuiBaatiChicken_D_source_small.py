def read():
    T = int(input())
    Ks = []
    Cs = []
    Ss = []
    for i in range(0,T):
        line = input().split()
        Ks.append(int(line[0]))
        Cs.append(int(line[1]))
        Ss.append(int(line[2]))
    for i in range(0,T):
        print('Case #'+str(i+1)+':', end = '')
        for j in range(1,Ks[i]+1):
            print(' '+str(j), end = '')
        print()

read()
