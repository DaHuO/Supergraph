def pancake(a):
    count=0
    flipcount=0
    for i in range(len(a)-1):
        if a[i]=="-" :
            if a[i+1]== "-":
                continue
            elif a[i+1]=="\n":
                count=1+count+flipcount
                return count
            else :
                flipcount+=1+count
                count=0
                continue
        else :
            if a[i+1]== "+":
                continue
            elif a[i+1]=="\n":
                count=count+flipcount
                return count
            else :
                count=0
                flipcount+=1+count
                continue
a=open("input.txt","r")
b=open("output.txt","w")
inp=list(a)
inp[len(inp)-1]+="\n"
for i in range(1,int(inp[0])+1,1):
    wr="case #"+str(i)+":  "+str(pancake(inp[i]))+"\n"
    b.write(wr)
