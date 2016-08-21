infile = open('A-large.in')
outfile = open('A-output.txt', 'w')

cases = int(infile.readline())
for t in range(cases):
    ref = []    
    n = int(infile.readline())
    index = 1
    while n > 0 and len(ref) < 10:
        cur_num = str(n * index)
        for i in range(len(cur_num)):
            if cur_num[i] not in ref:
                ref.append(cur_num[i])
        index += 1
    if len(ref) == 10:
        outfile.write("Case #%d: %s\n" % (t+1, cur_num))
    else:
        outfile.write("Case #%d: %s\n" % (t+1, "INSOMNIA"))
        
outfile.close()