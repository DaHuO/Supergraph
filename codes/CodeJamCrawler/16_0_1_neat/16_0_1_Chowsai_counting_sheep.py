file = open("A-large.in","r")
contents = file.readlines()
numbers = contents[0].strip()
ns= [contents[i].strip() for i in range(1,int(numbers)+1)]
results=[]


def cs(n):
    seen=[]
    counter=0
    if n==0:
        return 'INSOMNIA'
    else:
        while len(seen)<10:
            counter+=1
            say=counter*n
            said=str(say)
            for k in said:
                if k not in seen:
                    seen.append(k)
    return say

          
for n in ns:
    n=int(n)
    results.append(cs(n))


file.close()
file=open("cs_test_out.txt","w")
for i in range(int(numbers)):
    file.write("Case #{0}: {1}\n".format(i+1,results[i]))
file.close()
