# problem 11024
"""
n = int(raw_input())
for i in range(n):
    print sum(map(int, raw_input().split()))
"""
# problem 1002
"""
a = []
for i in range(input()):
    a.append(map(int,raw_input().split()))

    d = pow(a[i][0]-a[i][3],2) + pow(a[i][1]-a[i][4],2)
    x = pow(a[i][2]+a[i][5],2)
    y = pow(a[i][2]-a[i][5],2)

    if d == 0 and a[i][2] == a[i][5]:
        print -1
    elif x == d or y == d:
     print 1
    elif x < d or y > d:
        print 0
    else:
        print 2
"""
# problem 11718 not done
"""
while(1):
    a = raw_input()
    if len(a) == 0:
        break
    print a
"""
# problem 11066


"""
# problem 11531

cnt = 0

while(1):
    a = raw_input().split()
    if a[0]=='-1':
        break
    if a[2]=='right':
        cnt+=1
"""

# CodeJam #1
digit = [0,0,0,0,0,0,0,0,0,0]

cnt = 1
f = open('A-large.txt','r')
fw = open('A-large.out','w')
T = f.readline()

for i in range(int(T)):
    N = f.readline()
    if not N:
        break
    print N

    while True:
        if int(N) == 0:
            fw.write('Case #'+str(i+1)+': '+'INSOMNIA\n')
            break
        n = int(N)*cnt
        x = 10**(len(str(n))-1)
        #print x
        while x>=1:
            k = n/x
            #print n,k
            n = n-(k*x)
            x = x/10
            if digit[k] == 0:
                digit[k] += 1
        if sum(digit) == 10:
            digit = [0,0,0,0,0,0,0,0,0,0]
            fw.write('Case #'+str(i+1)+': '+str(int(N)*cnt)+'\n')
            cnt = 1
            break
        cnt+=1

f.close()
fw.close()