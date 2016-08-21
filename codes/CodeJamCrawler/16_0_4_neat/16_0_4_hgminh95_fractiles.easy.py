from sys import argv

_, infile, outfile = argv

out = open(outfile, 'w')

with open(infile, 'r') as lines:
    n = int(lines.readline())
    for i in range(n):
        numbers = lines.readline().split(' ')
        print numbers        

        k = int(numbers[0])
        c = int(numbers[1])
        s = int(numbers[2])

        out.write("Case #{0}: ".format(i + 1))
        
        if (k == 1):
            dist = 0
        else:
            dist = (k ** c - k) / (k - 1)
        curr = 1
        for j in range(k):
            out.write("{0} ".format(curr)) 
            
            curr += dist + 1
        out.write("\n")

    out.close()
