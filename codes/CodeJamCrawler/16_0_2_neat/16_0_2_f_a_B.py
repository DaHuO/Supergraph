infile = open('B-large.in')
outfile = open('B-output.txt', 'w')

opp = {'+': '-', '-': '+'}

cases = int(infile.readline())
for t in range(cases):
    count = 0
    sequence = infile.readline().strip()
    i = len(sequence)-1
    while (i >= 0):
        if (sequence[i] == '+'):
            i -= 1
        else:
            temp = ""
            while (sequence[i] != '+'):
                i -= 1
                if (i<0):
                    break
            count += 1
            for j in range(i+1):
                temp += opp[sequence[j]]
            sequence = temp
            i = len(sequence)-1
        
    outfile.write("Case #%d: %d\n" % (t+1, count))
    
outfile.close()
