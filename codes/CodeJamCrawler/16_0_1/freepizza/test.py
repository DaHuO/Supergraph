#!/usr/bin/python

# Open a file
#fo = open("input.txt", "r+")
fo = open("A-large.in", "r+")
#str1 = fo.read();
f=open("output.txt","w")
#f.write(str1);

t=int(fo.readline())
for i in range(t):
    n=int(fo.readline())
    if(n==0):
        f.write("case #"+str(i+1)+": INSOMNIA\n")
    else:
        l=[int(j) for j in range(10)]
        L=[]
        temp=n
        while(len(l)>0):
            s=list(set(str(temp)))
            s_length=len(s)
            for j in range(s_length):
                for k in range(len(l)):
                    con=int(s[j])
                    if(con==l[k]):
                        L.append(k)
                for j in L:
                    del(l[j])
                L=[]
            temp+=n
        f.write("case #"+str(i+1)+": "+str(temp-n))
	f.write("\n")
# Close opend file
fo.close()