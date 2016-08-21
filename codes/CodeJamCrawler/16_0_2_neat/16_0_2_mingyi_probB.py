import sys
filename=sys.argv[1:][0]

myFile = open(filename,'r')
L=[]
for i in myFile:    
    L.append(i.strip("\n"))
testnum=int(L[0])
L =L[1:]

def flin(S,n):
    D={"+":"-","-":"+"}
    L="".join(list(map(lambda x:D[x],S[:n])))
    SS=L+S[n:]
    return SS

def flipup(s):
    count =0
    n=len(s)
    while all(i=="+" for i in s)!= True and n>=0:
        if s[n-1]=="-":
            count+=1
            s = flin(s,n)
        n+=(-1)
            
    else:
        return str(count)
        
with open('ans.txt', 'w', newline="\n") as f:
    i = 0
    while i < testnum:
        ans = flipup(L[i])
        text ="Case #"+str(i+1)+": "+ans+"\n"
        f.write(text)
        i+=1
