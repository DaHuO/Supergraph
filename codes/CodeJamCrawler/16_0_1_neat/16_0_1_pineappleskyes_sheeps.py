file = open("A-large.in", 'r')
outfile = open("OUT.txt", 'w')
cases = int(file.readline())
n = []
for i in range(cases):
    n.append(int(file.readline()))

for x in range(cases):
    if n[x] == 0:
        outfile.write("Case #" + str(x+1) + ": INSOMNIA")
        outfile.write('\n')
    else:
        arr = [0,1,2,3,4,5,6,7,8,9]
        count = 0
        while len(arr) != 0:
            count += 1
            num = list(str(count * n[x]))
            for j in num:
                if int(j) in arr:
                    arr.remove(int(j))
            
        outfile.write("Case #" + str(x+1) + ": " + str(count*n[x]))
        outfile.write('\n')

file.close()
outfile.close()
