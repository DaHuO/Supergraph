file = open("A-large.in","r")
contents = file.readlines()
numbers = contents[0].strip()
ss = [contents[i].strip() for i in range(1,int(numbers)+1)]
results=[]

for s in ss:
    result=s[0]
    for i in range(1,len(s)):
        if ord(s[i])>=ord(result[0]):
            result=s[i]+result
        else:
            result=result+s[i]
    results.append(result)

file = open("A-large.out","w")

for a in range(len(results)):
    file.write("Case #{0}: {1}\n".format(a+1,results[a]))
file.close()
