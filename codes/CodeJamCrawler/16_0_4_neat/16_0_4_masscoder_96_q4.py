

def checking(r):
    s=''
    for i in range(r[0]):
        s= s+ str(i+1)
        s= s+' '
    return s
    


t=int(raw_input())
for i in range(t):
    #input list
    a=(map(int, raw_input().split()))
    print "Case #{}: {}".format(i+1, checking(a).strip())
