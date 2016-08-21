fin = open('A-large.in','r')
fout = open('A-large.out','w')

def countSheep(n):
    if n == 0:
        return "INSOMNIA"
    
    digCounts = [0]*10
    nums = [i for i in range(10)]

    i = 1

    while i > 0:
        #print(digCounts,nums)
        myNum = n*i
        for x in str(myNum):
            x = int(x)
            if digCounts[x] == 0:
                nums.remove(x)
            digCounts[x] += 1
        if nums == []:
            return str(myNum)
        else:
            i += 1
cases = int(fin.readline())

for c in range(cases):
    fout.write("Case #%d: %s\n" %(c+1, countSheep(int(fin.readline()))))
    print("Done case %d" %(c+1))

fin.close()
fout.close()
print("Execution complete.")


