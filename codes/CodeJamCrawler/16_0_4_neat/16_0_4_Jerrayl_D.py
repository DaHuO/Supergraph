file = open("D-small-attempt5.in","r")
contents = file.readlines()
number_of_lines = contents[0].strip()
lines = [contents[i].strip() for i in range(1,int(number_of_lines)+1)]
file.close()
results=[]

for line in lines:
    temp=[]
    values = line.split()
    K=int(values[0])
    C=int(values[1])
    for i in range(K):
        temp.append(str(i*(K**(C-1))+1))
    results.append(temp)
    temp=[]



file=open("D-small-attempt5.out","w")
for a in range(len(results)):
    file.write("Case #{0}: {1}\n".format(a+1,(" ").join(results[a])))
file.close()
        
