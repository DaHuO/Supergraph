f=open('Test.in', 'r')
out=open('out.out','w')
T=int(f.readline())

def pancake(s):
    n=len(s)-1
    a=list(map(lambda x: x=='+' ,s[:n]))
    count =0
    while(sum(a)!=n):
        i=a.index(False)
        if True in a:
            j=a.index(True)
            if i < j:
                i=j
            b=list(map(lambda x: x==False,a[:i]))
            a=b+a[i:]
        else:
            a=list(map(lambda x:x==False,a))
        count+=1
    print(count)
    return count
for i in range(T):
    out.write( "Case #"+str(i+1)+": "+str(pancake(f.readline()))+"\n")
