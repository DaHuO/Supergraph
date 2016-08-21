file = open("B-large.in","r")
contents = file.readlines()
number = contents[0].strip()
inputs = [contents[i].strip() for i in range(1,int(number)+1)]
results=[]

def pancake(n):
    if "-" not in n:
        return 0
    else:
        sign=n[0]
        result=0
        for i in range(1,len(n)):
            if n[i]!=sign:
                result+=1
                sign=n[i]
        if sign=="-":
            result+=1
        return result

for n in inputs:
    results.append(pancake(n))

file.close()
file = open("B-large.out","w")

for i in range(int(number)):
    file.write("Case #{0}: {1}\n".format(i+1,results[i]))
file.close()

