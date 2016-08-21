import re



def flip(stack,b,target):
    c=-1
    while(c<=b):
        c+=1
        stack[c]=target
    return stack

def pans(given):
    results=""
    stack=list(given)
    
    p=0
    flips=0
    if stack:
        active=stack[0]

    while(p<len(stack)-1):
        p+=1
        if not active==stack[p]:
            flips+=1
            target=stack[p]
            stack=flip(stack,p-1,target)
            active=target

    if stack[0]=='-': #catch one last:)
        stack=flip(stack,p-1,'+')
        flips+=1
    
    return flips

def main():
    filename="1in.dat"
    output="1out.dat"
    fo=open(output,'w')
    fp=open(filename,'r')

    c=-1
    for line in fp.readlines():
        c+=1
        line=re.sub(r'\n','',line)
    
        if c>0:
            result=pans(line)
            print "For: "+str(line)+"-> Case #"+str(c)+": "+str(result)
            
            fo.write("Case #"+str(c)+": "+str(result)+"\n")

    fo.close()

    return

if __name__ == '__main__':            
    main()
   


