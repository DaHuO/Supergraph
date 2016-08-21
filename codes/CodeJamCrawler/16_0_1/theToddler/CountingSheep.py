M = open("A-small-attempt1.in.txt")
lines = M.readlines()
nLines = len(lines)
M.close()
import sys
sys.stdout = open("A-small-attempt1.out.txt","w")
def calc(N):
    d = [0,0,0,0,0,0,0,0,0,0]
    j = 1;
    while(sum(d)< 10):
        n = j*N
        for i in str(n):
            if(d[int(i)] == 0):
                d[int(i)] = 1
        j += 1
    return str(n)  
t = int(lines[0])
for i in range(t):
    N = int(lines[i+1])
    if(N == 0):
        print("Case #"+ str(i+1)+": INSOMNIA")
    else :
        print("Case #"+ str(i+1)+": "+ calc(N))