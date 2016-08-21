file = open("A-large.in","r")
contents = file.readlines()
numbers = contents[0].strip()
ns = [contents[i].strip() for i in range(1,int(numbers)+1)]
results = []

def counting(n):
    counter = 1
    if n == 0:
        return "INSOMNIA"
    digits = [0,1,2,3,4,5,6,7,8,9]
    while True:
        number = n * counter
        while number > 0:
            if number % 10 in digits:
                digits.remove(number % 10)
            number = number // 10
        if digits == []:
            return n * counter
        counter += 1

for n in ns:
    results.append(counting(int(n)))

file.close()
file = open("A-large.out", "w")
for i in range(int(numbers)):
    file.write("Case #{0}: {1}\n".format(i+1,results[i]))
file.close()


