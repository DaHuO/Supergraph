import fileinput
f=fileinput.input()

def checkplus():
    e=0
    while(e+1<=len(n)-1):
        if(n[e+1]!='-'):
            e+=1
        else:
            break
    return e

def checkminus():
    e=0
    while(e+1<=len(n)-1):
        if(n[e+1]!='+'):
            e+=1
        else:
            break
    return e

def flipplus(e):
    i=0
    while(i<=e):
        n[i]='-'
        i+=1

def flipminus(e):
    i=0
    while(i<=e):
        n[i]='+'
        i+=1

t= int(f.readline())
s=t+1
while(t>0):
    n=str(f.readline())
    n=list(n)
    if(len(n)==1):
        if(n[0]=='+'):
            print "Case #{}: 0".format(s-t)
        else:
            print "Case #{}: 1".format(s-t)
        t-=1
        continue

    result=0
    while(1):
        if(n[0]=='+'):
            end=checkplus()
            if(end==len(n)-1):
                print "Case #{}: {}".format(s-t,result)
                break
            else:
                flipplus(end)
                result+=1
                continue
        else:
            end=checkminus()
            flipminus(end)
            result+=1
            continue

    t-=1



