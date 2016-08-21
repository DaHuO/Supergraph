t=int(input())
s=1
while s<=t:
    st=input()
    op=str(st[0])
    for i in range(1,len(st)):
        if st[i] < op[len(op)-1] or st[i]<op[0]:
            op+=str(st[i])
        else:
            op=st[i]+op
    print('Case #',s,': ',op,sep='')
    s+=1
