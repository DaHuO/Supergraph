t = int(input())
for i in range(1,t+1):
    k,c,s = map(int,input().split())
    r = ' '.join(map(str,range(1,k+1)))
    print('Case #%d: %s' %(i,r))
