def main():
    f=open('input1.txt','r')
    n=int(f.readline())
    testcases=[]
    for i in range(n):
        p=f.readline().rstrip('\n')
        l=f.readline().rstrip('\n').split()
        r=[]
        testcases.append(calculate(p,l,r))
    #print testcases
    #return
    fo=open('output1.txt','w+')
    for i in range(n):
        print 'Case #{0}: {1}'.format(i+1," ".join(testcases[i]))
        fo.write('Case #{0}: {1} \n'.format(i+1," ".join(testcases[i])))
#    print testcases

def calculate(p,l,r):
    #print "R",r
    #input(l)
    l=map(int,l)
    if sum(l)>0:
        half=sum(l)/2
        first=l.index(max(l))+65
        l[l.index(max(l))]=l[l.index(max(l))]-1
        half=sum(l)/2
        if max(l)>half:
            r.append(chr(first)+chr(l.index(max(l))+65))
            l[l.index(max(l))]=l[l.index(max(l))]-1
        else:
            r.append(chr(first))
        calculate(p,l,r)
        return r
    else:
        return r

    
if __name__=="__main__":
    main()