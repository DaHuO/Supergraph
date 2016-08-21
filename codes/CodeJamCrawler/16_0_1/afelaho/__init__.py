def CountingSheep():
    f = open('A-large.in')
    f2 = open('A-large.out','w+')
    T = int(f.readline())

    for k in range(1, T+1):
        myset = set()
        mylist = []
        j= 2
        breaking = 0
        N = int(f.readline())
        N2 = N
        while True:
            if N == 0: print >>f2,  "Case #"+str(k)+": INSOMNIA";break
            for i in str(N2):
                if i not in myset:
                    mylist.append(i)
                    myset.add(i)
                    if len(myset) == 10:print >>f2, "Case #" + str(k) + ": " + str(N2);breaking=1;break
            if breaking == 1: break
            N2 = N * j
            j += 1
#            if j > 100000: return

def main():
    CountingSheep()
    
main()
