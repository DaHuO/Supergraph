N = 0
final = []
def inp():
    N = int(input())

    for i in range(N):
        n = int(input())
        l = []
        for i in range(2*n - 1):
            p = [int(x) for x in input().split(' ')]
            for y in p:
                l.append(y)
        l.sort()
        f = []
        for i in l:
            if(l.count(i)%2 == 1):
                if(f.count(i)==0):
                    f.append(i)
        final.append(f)

    for i in range(N):
        print("Case #",i+1,": ",sep='',end='')
        for j in range(len(final[i])):
            print(final[i][j],end=' ')
        print('')
    
inp()
