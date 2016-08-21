from __future__ import print_function
log = open("a.txt", "w")
def jam():
    a=int(raw_input())
    while(a>0):
        cnt=0
        b=raw_input()
        l=[]
        k=[]
        if(b.find("+-")!=-1):
            cnt+=1
        if(b.find("-+")!=-1):
            cnt+=1

        l.append(b.find("+-"))
        k.append(b.find("-+"))


        for i in l:
            if(b.find("+-",i+1)!=-1):
                l.append(b.find("+-",i+1))
                cnt+=1

        for j in k:
            if(b.find("-+",j+1)!=-1):
                k.append(b.find("-+",j+1))
                cnt+=1
        if(b.find("+")==-1):
            cnt=1
        elif(b.find("-")==-1):
            cnt=0
        elif(b[-1]=='-'):
            if(len(b)!=1):
                cnt+=1

        print("Case #"+str(101-a)+": "+str(cnt))
        a-=1


jam()
