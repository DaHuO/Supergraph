file = open("A-large.in")
with open("output.txt","w") as output:
    total=file.readline()
    for i in range(1,int(total)+1):
        seenList=[]
        k=1
        N=file.readline()
        if int(N)<1:
            output.write("Case #"+str(i)+": "+"INSOMNIA\n")
            continue
        while len(seenList)<10:
            x=int(N)*k
            for j in str(x):
                if j not in seenList:
                    seenList.append(j)
                    
                    
            k+=1
        output.write("Case #"+str(i)+": "+str(x)+"\n") 
        
    

file.close()
