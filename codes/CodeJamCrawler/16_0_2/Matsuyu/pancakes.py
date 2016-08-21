file = open("B-large.in","r")
contents = file.readlines()
numbers = contents[0].strip()
ss = [contents[i].strip() for i in range(1,int(numbers)+1)]
results=[]

def pancakes(s):
    result=0
    sign=s[0]
    for i in range(len(s)):
        if s[i]!=sign:
            result+=1
            sign=s[i]
    if s[-1]=="-":
        result+=1
    return result

for s in ss:
    results.append(pancakes(s))

file.close()
file=open("B-large.out","w")
for i in range(int(numbers)):
    file.write("Case #{0}: {1}\n".format(i+1,results[i]))
file.close()
