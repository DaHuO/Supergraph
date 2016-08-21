



def getNumber(N):
    i=1
    numbers=["0","1","2","3","4","5","6","7","8","9"]
    while(1):
        
        if(N==0):
            return "INSOMNIA"
            break    
        
        for s in str(N*i):
            if s in numbers:
                numbers.remove(s)
        
        
        if len(numbers)==0:
            #print(N*i)
            return (N*i)
            break
        
        i+=1
        

out=open("A_result.txt","w+")
result =[]
with open("A-large.in") as f:
    lines = f.read().splitlines()
num_cases=int(lines[0])

for i in range(1,len(lines)):
    temp= "Case #" + str(i)+ ": " + str( getNumber(int(lines[i])))
        
    result.append(temp)     
out.write("\n".join(result))
out.close()