t=int(raw_input())
n=raw_input().split(" ");
j=int(n[1]);
n=int(n[0]);
i=0;
ff=[0,0,0,0,0,0,0,0,0];
m=1;
ss=[0,0,0,0,0,0,0,0,0];
fs=int("1"+"0"*(n-2)+"1",base=2);
ls=int("1"*n,base=2)

def prime(ptest): 
    primefound=1;
    maxPrimeSeek=int(ptest**(1/2.0))+1;
    if (ptest==2):
        return 0;
    if (ptest%2==0):
        return 2;
    for i in range(3,maxPrimeSeek,2):
        if (not (ptest%i)):
            primefound=0;
            break;
    if(primefound):
            return 0;
    else:
            return i;

def factor(x):
    fi=2
    while(1):
        if x % fi == 0:
            return fi;
        fi=fi+1;      
print "Case #1:"
for i in range(fs,ls+1):
    if(m>j):
        break;
    s="{0:b}".format(i);
    if(s[n-1]=='1'):
        ss[0]=int(s,base=2);
        ss[1]=int(s,base=3);
        ss[2]=int(s,base=4);
        ss[3]=int(s,base=5);
        ss[4]=int(s,base=6);
        ss[5]=int(s,base=7);
        ss[6]=int(s,base=8);
        ss[7]=int(s,base=9);
        ss[8]=int(s,base=10);

        ff[0]=prime(ss[0]);
        ff[1]=prime(ss[1]);
        ff[2]=prime(ss[2]);
        ff[3]=prime(ss[3]);
        ff[4]=prime(ss[4]);
        ff[5]=prime(ss[5]);
        ff[6]=prime(ss[6]);
        ff[7]=prime(ss[7]);
        ff[8]=prime(ss[8]);
        #print s+" "+str(ff[0])+" "+str(ff[1])+" "+str(ff[2])+" "+str(ff[3])+" "+str(ff[4])+" "+str(ff[5])+" "+str(ff[6])+" "+str(ff[7])+" "+str(ff[8]);

        if(not ff.count(0)):
            print s+" "+str(ff[0])+" "+str(ff[1])+" "+str(ff[2])+" "+str(ff[3])+" "+str(ff[4])+" "+str(ff[5])+" "+str(ff[6])+" "+str(ff[7])+" "+str(ff[8]);
            ff=[0,0,0,0,0,0,0,0,0];
            m=m+1;            
        else:
            continue;

        

