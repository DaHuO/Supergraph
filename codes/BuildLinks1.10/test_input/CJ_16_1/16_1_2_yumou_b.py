file=open("B-large.in")
k=file.readline()
a=int(k[:-1])
w=open("output.txt","w")
for num in range(a):
    k=int(file.readline()[:-1])
    dic={}
    for i in range((2*k-1)):
        line=file.readline()
        while True:
            n=line.find(" ")
            if n==-1:
                pp=int(line[:])
                if pp in dic:
                    dic[pp]+=1
                else:
                    dic[pp]=1
                break
            else:
                a+=1
                pp=int(line[0:n])
                if pp in dic:
                    dic[pp]+=1
                else:
                    dic[pp]=1
                line=line[n+1:]
    lst=[]
    for i in dic:
        if dic[i]%2==1:
            lst.append(i)
    lst.sort()
    ans=""
    for i in lst:
        ans+=" "+str(i)
    s="case #"+str(num+1)+":"+ans+"\n"
    w.write(s)
w.close()
            
