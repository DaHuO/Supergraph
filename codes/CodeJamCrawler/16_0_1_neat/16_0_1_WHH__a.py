infile = open("A-large.in", "r")
outfile = open("A-large.out", "w")

digits = [1,1,1,1,1,1,1,1,1,1]
t = infile.readline()
print(t)
count = 1
for line in infile:
    seen = [0,0,0,0,0,0,0,0,0,0]
    n = line[:-1]
    a = int(n)
    if n == '0':
        print("Case #{}: INSOMNIA".format(count), file=outfile)
        count+=1
        continue
    while seen!=digits:
        
        for i in range(len(str(n))):
            seen[int(str(n)[i])] = 1
            
        if seen == digits:
            print("Case #{}: {}".format(count, n), file=outfile)
        n = int(n)+ a
    count+=1

print("done")
infile.close()
outfile.close()
