t=int(raw_input())
l={''};
g=0;
d=1;
x=" ";
def check():
    c=list(l);
    c.sort();
    if (c==['','0','1','2','3','4','5','6','7','8','9']):
        return 1;
    else:
        return 0;
    
for i in range(t):
    n=int(raw_input());
    r=n;
    if(n==0):
        print "case #"+str(i+1)+": INSOMNIA";
    else:
        while(1):
            a=set(str(n))-l;
            l=l.union(a);
            d=check();
            if(d==0):
                n=(g+1)*r;
            else:
                break;
            g=g+1;
        print "case #"+str((i+1))+": "+str(n);
            
    g=1;
    l={''}
