def findnum(lis):
    for x in range(0,10):
        if x not in lis:
            return False
    return True

file1 = open('A-large.in','r')
d = file1.read().split("\n")[1:-1]
print(d)
d = [int(r) for r in d]
file = open("lol1.txt",'w')
s = 1

for n in d:
    file.write("Case #"+str(s)+": ")
    num = list(str(n))
    lis = [int(x) for x in num]
    z = 1
    if lis != [0]:
        while not findnum(lis):
            num = list(str(z*n))
            for l in num:
                lis.append(l)
            lis = [int(x) for x in lis]
            z+=1
        file.write("".join(num))
    else:
        file.write('INSOMNIA')
    if s != 100:
        file.write('\n')
    s+=1

file1.close()
file.close()
