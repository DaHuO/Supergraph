file = open("A-large.in","r")
contents = file.readlines()
numbers = contents[0].strip()
inputs = [contents[i].strip() for i in range(1,int(numbers)+1)]
results=[]

def last_word(n):
    x=n[0]
    for i in range(1,len(n)):
        if n[i]>=x[0]:
            x=n[i]+x
        else:
            x=x+n[i]
    return x

for i in inputs:
    results.append(last_word(i))

file.close()
file = open("A-large.out","w")

for a in range(len(results)):
    file.write("Case #{0}: {1}\n".format(a+1,results[a]))
file.close()


