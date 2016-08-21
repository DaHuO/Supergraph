f =open('out.txt', 'w')
f1=open('B-large.in', 'r')
p=f1.readlines()
t=int(p[0])
v=1
while t :
    t=t-1
    s=p[v]
    L=len(s)
    if '+' not in s:
        count=1
    elif '-' not in s:
        count=0
    else:
        count=0
        flag=0
        i=0
        while flag==0:
            srr=""
            start=s[0]
            while i+1<L and s[i+1]==start:
                i=i+1
            if start=='+':
                for ind in range(0,i+1):
                    srr=srr+'-'
                for ind in range(i+1,L):
                    srr=srr+s[ind]    
            else:
                for ind in range(0,i+1):
                    srr=srr+'+'
                for ind in range(i+1,L):
                    srr=srr+s[ind]    
            count=count+1
            if '-' in srr:
                flag=0
            else:
                flag=1
            s=srr
    v=v+1
    f.write("Case #")
    f.write(str(v-1))
    f.write(": ")
    f.write(str(count))
    f.write("\n")
f.close()
f1.close()
