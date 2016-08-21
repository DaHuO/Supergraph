import fileinput
cases = int(fileinput.input())
f=[]
last=0
newline=0
for i in range (10):
    f.append(0);
for x in range(1,cases+1):
    line=int(fileinput.input());
    newline=line
    if (line == 0):
        last = "Insomnia"
    else:
        for i in range(10):
            f[i]=0
            flag=1
            counter=1
        while(flag):
            check=newline
            while(check>0):
                remainder = int(check%10)
                check= int(check /10)
                f[remainder]=1
                mysum=0
            for i in range(10):
                mysum+=f[i]
            
            if(mysum ==10):
                flag=0
                last=newline
            else:
                counter+=1
                newline=line*counter
                
       
                
    print("Case #%i :%s" %(x,last))