import sys
filename = sys.argv[1:][0]

myFile = open(filename,'r')
L=[]
for i in myFile:    
    L.append(int(i.strip("\n")))
L =L[1:]


def fallasasleep(n):
    n=int(n)
    if n!=0:
        Q=list(map(lambda x:str(x),list(range(10))))
        i=1
        while Q!=[]:
            str_n=str(n*i)
            for j in str_n:
                if j in Q:
                    Q.remove(j)            
            i+=1
        return str_n           
    else:
        return "INSOMNIA"
        
with open('Failed.txt', 'w', newline="\n") as f:
    i = 0
    while i < len(L):
        ans = fallasasleep(L[i])
        text ="Case #"+str(i+1)+": "+ans+"\n"
        f.write(text)
        i+=1