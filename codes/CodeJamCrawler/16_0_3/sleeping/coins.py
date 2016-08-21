a=[]
def pr1(s,n):
    if not n:
        a.append('11'+s+'11')
        return
    pr1('00'+s,n-1)
    pr1('11'+s,n-1)

t=int(raw_input())
n,j=map(int,raw_input().split())
pr1('',n/2-2)
print "Case #1:"
for i in range(j):
    print a[i], " ".join(map(str,range(3,12)))
