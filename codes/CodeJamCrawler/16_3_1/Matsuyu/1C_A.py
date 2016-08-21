file = open("A-small-attempt0.in","r")
number= int(file.readline().strip())
results=[]
for i in range (number):
    n=int(file.readline().strip())
    words = file.readline().strip().split(' ')
    parties=[]
    total=0
    result=[]
    for i in range (n):
        parties.append([])
        parties[i].append(chr(65+i))
        parties[i].append(int(words[i]))
        total+=parties[i][1]
    from operator import itemgetter
    while total>0:
        parties=sorted(parties, key=itemgetter(1),reverse=True)
        if total==3:
            result.append(parties[0][0])
            parties[0][1]-=1
            total-=1
        else:
            if parties[1][1]>int((total-2)/2):
                result.append(parties[0][0]+parties[1][0])
                parties[0][1]-=1
                parties[1][1]-=1
                total-=2
            else:
                result.append(parties[0][0]*2)
                parties[0][1]-=2
                total-=2
    results.append(result)

file.close()


file = open("A-small-attempt0.out","w")

for a in range(len(results)):
    file.write("Case #{0}: {1}\n".format(a+1,' '.join(results[a])))
file.close()

    
