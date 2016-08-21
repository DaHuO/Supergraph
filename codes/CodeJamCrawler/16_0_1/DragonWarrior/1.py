n = input()
l = []

def rec(x,k,i):
    tt = x * i
    y = str(tt)
    for u in y:
        if( u in k):
            del(k[k.index(u)])
    if(len(k)==0):
        return y
    return rec(x,k,i+1)
    
for i in range(0,n):
    l.append(raw_input())

for t in l:
    if(t == '0'):
        print("Case #"+str(l.index(t)+1)+": INSOMNIA")
    else:
        k = ['0','1','2','3','4','5','6','7','8','9']
        print("Case #"+str(l.index(t)+1)+": "+rec(int(t),k,1))
