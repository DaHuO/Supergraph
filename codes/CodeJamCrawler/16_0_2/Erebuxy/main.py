import math

num = int(raw_input())
for i in range(1,num+1):
    n = raw_input()
    l = len(n)
    count = 0
    cur = 0
    for j in range(l-1,-1,-1):
        if cur == 0 and n[j] == '-':
            cur = 1
            count += 1
        elif cur == 1 and n[j] == '+':
            cur = 0
            count += 1
    print "Case #"+str(i)+":", count
            