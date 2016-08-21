#import sys
#sys.stdout = open("a.txt", "w")
from __future__ import print_function
log = open("a.txt", "w")

def jam():
    a=int(raw_input())
    while(a>0):
        l={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        b=raw_input()
        if(b=='0'):
            print("Case #"+str(101-a)+": INSOMNIA", file = log)
            a-=1
            continue
        init=int(b)
        ch=True
        cnt=0
        ir=1
        while(ch):
            for i in b:
                l[i]+=1
            for i in l:
                if(l[i]!=0):
                    cnt+=1
            if(cnt==10):
                print("Case #"+str(101-a)+": "+b, file = log)

                ch=False
            else:
                cnt=0
                ir+=1
                b=str(int(b)+init)
        a-=1


jam()
