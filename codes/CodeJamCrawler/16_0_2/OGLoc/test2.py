
def flip(s,n):         # s is the string # n number of first bits to flip
    t=""
    for i in s:
        if(i=="+" and n>0):
            t+="-"
            n-=1
        elif(i=="-" and n>0):
            t+="+"
            n-=1
        else:
            t+=i
    return t
    
def flipNum(s):
    ans = "+"*len(s)
    temp=s
    count = 0
    for i in range(len(temp)-1,-1,-1):
        if(ans==temp):return count
        if temp[i]=="+":continue
        else:
            temp=flip(temp,i+1)
            count+=1
    return count
        
inputf=open("B-large.in","r")
outputf = open("output.txt","w")
s=inputf.read().split()

for i in range(int(s[0])):
    outputf.write("Case #"+str(i+1)+": "+str(flipNum(s[i+1]))+"\n")
    
outputf.close()
inputf.close()
    

