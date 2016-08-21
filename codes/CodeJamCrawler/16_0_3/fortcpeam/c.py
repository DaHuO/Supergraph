import random
#import math

N = 16
J = 50

#st = "1000000000000001"
#st = "10000000000000000000000000000001"

ans = []
dv = []
st = []

def Check(x):
    for i in range(2, x):
        if (x % i == 0):
            return i
        if (i * i > x):
            return 0
    return 0

fo = open('c.out', 'w')

for i in range(0, N):
    st.append(1)
    
for i in range(0, 20):
    dv.append(i)
    
sz = 0
while (sz < J):
    
    x = 1
    for i in range(1, N-1):
        st[i] = random.randint(0, 1)
        x = x * 10 + st[i]
    x = x * 10 + 1
        
    #check if x already exists
    same = False
    for i in range(0, sz):
        if (ans[i] == x):
            same = True
            break
    if (same):
        continue

    valid = True    
    for i in range(2, 11):
        x = 1
        for j in range(1, N):
            x = x * i + st[j]
        dv[i] = Check(x)
        if (dv[i] == 0):
            valid = False
            break

    if (valid == False):
        continue

    fo.write (repr(x))
    for i in range(2, 11):
        fo.write (" " + repr(dv[i]))
    fo.write('\n')

    print ("Check: ", x, "\n")
    
    ans.append(x)
    sz += 1

#print (len(st))

fo.close()
