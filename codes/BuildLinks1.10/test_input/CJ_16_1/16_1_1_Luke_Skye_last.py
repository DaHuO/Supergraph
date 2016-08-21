fi=open("A-large.in","r")
fo=open("output.txt","w")

t=int(fi.readline().strip())

t1=1

while t1<=t:
    s=fi.readline().strip()
    res=''
    for c in s:
        if res=='':
            res=res+c
        else:
            if c >=res[0]:
                res=c+res
            else :
                res=res+c
    fo.write("Case #%d: %s\n" %(t1,res))
    
    t1+=1
    
    
    
    