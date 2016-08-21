T = int(input())
Case = []
for i in range(T):
    j = int(input())
    Case.append(j)
for i in range(len(Case)):
    flag0 = 0
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    flag5 = 0
    flag6 = 0
    flag7 = 0
    flag8 = 0
    flag9 = 0
    summa = 0
    Old_N = Case[i]
    N = Old_N
    t = 1
    if N == 0:
        print('Case #',i+1,': ','INSOMNIA',sep='')
        continue
    while summa != 10:
        if '0' in str(N):
            flag0 = 1
        if '1' in str(N):
            flag1 = 1        
        if '2' in str(N):
            flag2 = 1            
        if '3' in str(N):
            flag3 = 1            
        if '4' in str(N):
            flag4 = 1
        if '5' in str(N):
            flag5 = 1
        if '6' in str(N):
            flag6 = 1
        if '7' in str(N):
            flag7 = 1
        if '8' in str(N):
            flag8 = 1      
        if '9' in str(N):
            flag9 = 1 
        summa = flag0 + flag1 + flag2 + flag3 + flag4 + flag5 + flag6 + flag7 +flag8 + flag9
        if summa == 10:
            print('Case #',i+1,': ',N,sep='')
        t+=1
        N = Old_N * t
    