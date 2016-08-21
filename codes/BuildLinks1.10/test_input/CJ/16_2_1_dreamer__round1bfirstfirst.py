t=int(raw_input())
ck=["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
tcount=0
d={0:'Z',1:'O',2:'W',3:'T',4:'U',5:'F',6:'X',7:'V',8:'G',9:'N'}
m=[0,2,4,6,8]
n=[1,3,5,7,9]
while t:
    s=raw_input()
    l=list(s)
    ans=[]
    for i in m:
        while True:
            if d[i] in l:
                for k in ck[i]:
                    l.remove(k)
                ans.append(str(i))
            else:
                break
    for i in n:
        while True:
            if d[i] in l:
                for k in ck[i]:
                    l.remove(k)
                ans.append(str(i))
            else:
                break
    ans=sorted(ans)
    print "Case #"+str(tcount+1)+": "+''.join(ans)
    t-=1
    tcount+=1
        
            
