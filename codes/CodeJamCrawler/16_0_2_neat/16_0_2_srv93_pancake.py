import sys, numpy as np

count = 0
def flip(array, n):
    global count
    count += 1
    return np.append(-array[n::-1], array[n+1:])

input = [x.strip() for x in sys.stdin.readlines()][1:]

for i,ip in enumerate(input):
    input[i] = np.array([-1 if x=='-' else 1 for x in ip])
    
for case, ip in enumerate(input):
    N = len(ip)
    count = 0
    for j in range(N-1,-1,-1):
        if(ip[j]==-1):
            if(ip[0]==-1):
                ip = flip(ip,j)
            else:
                i = 1
                while ip[i]==1 and i<N:
                    i+=1
                ip = flip(ip,i-1)
                ip = flip(ip,j)
    print 'Case #'+str(case+1)+': '+str(count)
