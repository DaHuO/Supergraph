t=int(raw_input())
kk = [2,8,0,6,4,1,3,5,9,7]
l = ["TWO", "EIGHT", "ZERO", "SIX", "FOUR", "ONE", "THREE", "FIVE", "NINE", "SEVEN"]
for i in xrange(t):
    dict={}
    li=[]
    s = str(raw_input())

    for a in s:
        if dict.has_key(a):
            dict[a]+=1
        else:
            dict[a]=1
    p=0
    while p < len(l):
        flag=0
        temp=dict.copy()
        for k in range(len(l[p])):
            if not temp.has_key(l[p][k]):
                flag=1
                break
            else:
                if temp[l[p][k]]!=0:
                    temp[l[p][k]]-=1
                else:
                    flag=1
                    break
        if flag==1:
            p+=1
            continue
        flag=0
        for c in l[p]:
            if dict.has_key(c):
                if dict[c]!=0:
                    dict[c]-=1
        li.append(str(kk[p]))
    li.sort()
    print('Case #'+str(i+1)+': '+''.join(li))
