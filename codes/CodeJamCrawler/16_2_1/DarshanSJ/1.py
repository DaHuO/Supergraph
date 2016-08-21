t=input()
case=1

digits=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

def calc(i,inp,out):
    global output
    if len(inp)==0:
        output=out
        return True
    if i==10 and len(inp)!=0:
        return False
    there=True
    for j in digits[i]:
        if j not in inp:
            there=False
            break
    res=False
    if there:
        n=inp[:]
        for j in digits[i]:
            try:
                n.remove(j)
            except:
                there=False
                return calc(i+1,inp,out)
        x=calc(i,n,out+str(i))
        res=x
        if not x:
            y=calc(i+1,n,out+str(i))
            res=y
            if not y:
                res=calc(i+1,inp,out)
    else:
        res=calc(i+1,inp,out)
    return res
         

while case<=t:
    inp=raw_input().strip()
    inp=list(inp)
    output=''
    calc(0,inp,'')
    print 'Case #'+str(case)+": "+output
    case+=1
