nums=["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]

def f(s, n):
    if s=="":
        return ""
    if n>9:
        return None
    flag=True
    cnt=0
    t=s
    while flag:
        res=f(t, n+1)
        if res!=None:
            return cnt*str(n)+res
        r=True
        for c in nums[n]:
            if nums[n].count(c)>t.count(c):
                r=False
                break
        if r:
            temp=""
            cnt=cnt+1
            for c in nums[n]:
                if not c in temp:
                    temp+=(t.count(c)-nums[n].count(c))*c
            for c in t:
                if not c in temp and not c in nums[n]:
                    temp+=c
            t=temp
        else:
            flag=False
            

TT=int(input())+1
for T in range(1, TT):
    s=input()
    print("Case #"+str(T)+": ")
    print(f(s,0))