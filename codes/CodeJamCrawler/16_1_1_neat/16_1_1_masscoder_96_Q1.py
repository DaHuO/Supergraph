

def word(a):
    ls=list(a)
    out=[]
    c=0
    
    for  i in ls:
        if c==0:
            out.append(i)
        check=[]
        if c!=0:
            check.append(out[0])
            check.append(i)
            if out[0]>i:
                out.append(i)
            else:
                ss= i+''.join(out)
                out=list(ss)
        c+=1
    return ''.join(out)

















t = int(raw_input())
for i in range(t):
    a = raw_input().strip()
    print "Case #{}: {}".format(i+1, word(a))
