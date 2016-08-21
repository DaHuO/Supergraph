import re




def seenit(given):
    #perf:  ideally, better search
    given=int(given)

    result="INSOMNIA"
    last=-1
    seen=[]
    c=1
    while(c):
        v=c*given
#d        print "> "+str(v)+" seen: "+str(seen)+" len "+str(len(seen))
        
        if str(v)==str(last):
            result="INSOMNIA"
            break
        
        for k in str(v):
            if not k in seen:
                seen.append(k)
            if len(seen)==10:
                result=str(v)
                c=-1
        last=str(v)

        c+=1

    return result

def main():
    filename="1in.dat"
    output="1out.dat"
    fo=open(output,'w')
    fp=open(filename,'r')
    #fp=['0','1','2','11','1692']

    c=-1
    for line in fp.readlines():
        c+=1
        line=re.sub(r'\n','',line)
    
        if c>0:
            result=seenit(line)
            print "For: "+str(line)+"-> Case #"+str(c)+": "+str(result)
            
            fo.write("Case #"+str(c)+": "+str(result)+"\n")

    fo.close()

    return

if __name__ == '__main__':            
    main()
   


