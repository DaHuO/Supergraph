input_N = []
f = open("A-large.in", "r")
g = open("A-largeout.txt", "w")
for line in f:
    input_N.append(int(line))
totalList = [0,1,2,3,4,5,6,7,8,9]
output_N = []

def counting(s):
    if s == 0:
        return "INSOMNIA"
    else:
        numList = []
        i=0
        while sorted(numList) != totalList:
            d = s
            i += 1
            d *= i
            for x in range(0,len(str(d))):
                a = int(str(d)[x])
                if a not in numList:
                    numList.append(a)
        return s*i

for x in range(1,len(input_N)):
    g.write("Case #%s: %s\n" %(x, counting(input_N[x])))

f.close()
g.close()
