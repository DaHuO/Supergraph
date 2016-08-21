file = open("B-large.in","r")
contents = file.readlines()
number_of_lines = contents[0].strip()
lines = [contents[i].strip() for i in range(1,int(number_of_lines)+1)]
file.close()
results=[]


def flip(pancakes):
    flipped=""
    for i in pancakes:
        if i=="-":
            flipped+="+"
        else:
            flipped+="-"
    return flipped


for pancakes in lines:
    n=0
    while "-" in pancakes:
        for i in range(len(pancakes)-1,-1,-1):
            if pancakes[i]=="-":
                pancakes=flip(pancakes[:i+1])+pancakes[i+1:]
                break
        n+=1
    results.append(n)


file=open("B-large.out","w")
for a in range(len(results)):
    file.write("Case #{0}: {1}\n".format(a+1,results[a]))
file.close()
        
