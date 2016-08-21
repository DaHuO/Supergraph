file = open("A-large.in","r")
contents = file.readlines()
number = contents[0].strip()
integers = [contents[i].strip() for i in range(1,int(number)+1)]
results=[]

def counting_sheep(n):
    if n==0:
        return 'INSOMNIA'
    else:
        a=[0,1,2,3,4,5,6,7,8,9]
        i=0
        while len(a)!=0:
            i=i+1
            k=n*i
            while k!=0:
                digit=k%10
                if digit in a:
                    a.remove(digit)
                k=k//10
        return n*i

for n in integers:
    results.append(counting_sheep(int(n)))

file.close()
file = open("A-large.out","w")

for i in range(int(number)):
    file.write("Case #{0}: {1}\n".format(i+1,results[i]))
file.close()
