file = open("A-large.in","r")
contents = file.readlines()
numbers = contents[0].strip()
ns = [contents[i].strip() for i in range(1,int(numbers) + 1)]
results=[]

def count_sheep(n):
    i = 1
    if n == 0:
        return "INSOMNIA"
    array = [0,1,2,3,4,5,6,7,8,9]
    while True:
        num = n * i
        while num > 0:
            if num % 10 in array:
                array.remove(num % 10)
            num = num // 10
        if array == []:
            return n * i
        i += 1

for n in ns:
    results.append(count_sheep(int(n)))

file.close()
file = open("A-large.out","w")
for i in range(int(numbers)):
    file.write("Case #{0}: {1}\n".format(i + 1, results[i]))
file.close()
