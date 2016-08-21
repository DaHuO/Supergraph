def check3(ups):
    for i in range(len(ups)):
        if ups[i]=='-':
            return True
    return False


def removecontplus(ups):
    templ=[]
    templ.append(ups[0])
    for i in range(1,len(ups),1):
        if ups[i]=='+' and ups[i-1]=='+':
            continue
        else:
            templ.append(ups[i])
    toret=''.join(templ)
    return toret


def removecontminus(ups):
    templ=[]
    templ.append(ups[0])
    for i in range(1,len(ups),1):
        if ups[i]=='-' and ups[i-1]=='-':
            continue
        else:
            templ.append(ups[i])
    toret=''.join(templ)
    return toret

def check2(ups):
    for i in range(len(ups)-1,-1, -1):
        if(ups[i]=='-'):
            break
    return ups[0:i+1]


t=open("B-small-attempt3.in")
t1=open("out6.txt", "wb")

text=t.read()
inputlist=text.split("\n")

n=int(inputlist[0])
for i in range(n):
    ups=inputlist[i+1]
    if check3(ups)==False:
        ans=0
        t1.write("Case #{}: {}".format(i+1, ans))
        t1.write("\n")
        continue
    ups=removecontplus(ups)
    ups=removecontminus(ups)
    ups=check2(ups)
    totallen=len(ups)
    t1.write("Case #{}: {}".format(i+1, totallen))
    t1.write("\n")

t.close()
t1.close()
