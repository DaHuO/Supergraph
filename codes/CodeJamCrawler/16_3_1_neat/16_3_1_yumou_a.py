def dafacai(lst):
    su=0
    ans=""
    for i in lst:
        su+=i
    if su%2==1:
        ans+=magic1(lst)+" "
    turn=(su//2)
    for i in range(turn):
        ans+=magic(lst)+" "
    return ans[:-1]

def magic(lst):
    w=[]
    for i in range(len(lst)):
        w.append([i,lst[i]])
    w.sort(key=lambda x:x[1])
    w.reverse()
    lst[w[0][0]]-=1
    lst[w[1][0]]-=1
    return(chr(w[0][0]+65)+chr(w[1][0]+65))

def magic1(lst):
    w=[]
    for i in range(len(lst)):
        w.append([i,lst[i]])
    w.sort(key=lambda x:x[1])
    w.reverse()
    lst[w[0][0]]-=1
    return(chr(w[0][0]+65))




file=open("A-large.in")
k=file.readline()
a=int(k[:-1])
w=open("output.txt","w")



for num in range(a):
    k=file.readline()[:-1]
    lst=str(file.readline()[:-1])
    lst=lst.split()
    for i in range(len(lst)):
        lst[i]=int(lst[i])
    ans=dafacai(lst)
    s="case #"+str(num+1)+": "+ans+"\n"
    w.write(s)
w.close()




        
