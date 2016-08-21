inpfile=open("E:\Abhishek\Google Code Jam\Qualification round\A-large.txt","r")
outfile=open("E:\Abhishek\Google Code Jam\Qualification round\largeoutput.txt","w")
T=int(inpfile.readline())
if(1<=T<=100):
    print T
    for z in range (1,T+1,1):
        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        g=0
        h=0
        i=0
        j=0
        N=int(inpfile.readline())
        x=1
        if N==0 :
            n="INSOMNIA"
        else:
            while (a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or g==0 or h==0 or i==0 or j==0):
                print a,b,c,d,e,f,g,h,i,j
                n=N*x
                s=N*x
                while (s>0):
                    y=s%10
                    s=s/10
                    if y==1 :
                        a=a+1
                    if y==2 :
                        b=b+1
                    if y==3 :
                        c=c+1
                    if y==4 :
                        d=d+1
                    if y==5 :
                        e=e+1
                    if y==6 :
                        f=f+1
                    if y==7 :
                        g=g+1
                    if y==8 :
                        h=h+1
                    if y==9 :
                        i=i+1
                    if y==0 :
                        j=j+1
                x=x+1
        print"Case #"+str(z)+": "+str(n)+"\n"
        outfile.write("Case #"+str(z)+": "+str(n)+"\n")
inpfile.close()
outfile.close()
