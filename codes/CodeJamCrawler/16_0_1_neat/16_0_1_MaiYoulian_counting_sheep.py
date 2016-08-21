file = open("A-large.in","r")
contents = file.readlines()
numbers = contents[0].strip()
ns = [contents[i].strip() for i in range(1,int(numbers)+1)]
results=[]

def counting_sheeps(n):
    i = 1
    if n == 0:
        return "INSOMNIA"
    digit = [0,1,2,3,4,5,6,7,8,9]
    while digit != []:
        number = n*i
        while number > 0:
            remainder = number % 10
            if remainder in digit:
                digit.remove(remainder)
            number = number//10
        i += 1

    return ((i-1) * n)

for n in ns:
    results.append(counting_sheeps(int(n)))

file.close()
file=open("A-large.out","w")
for i in range(int(numbers)):
    file.write("Case #{0}: {1}\n".format(i+1,results[i]))
file.close()
