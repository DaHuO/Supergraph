# find the missing note (numbers in increasing order)

infile = open("B-large.in",'r')
casenum = int(infile.readline())


ofile = open('B-large.txt','w')

for case in range(casenum):
    print 'Case #'+str(case+1)+'--------------'
    n = int(infile.readline().split('\n')[0])
    stat = {}
    for k in range(2*n-1):
        note = infile.readline().split('\n')[0].split(' ')
        for char in note:
            if char not in stat:
                stat[char] = 1
            else:
                stat[char] += 1
    res = []
    for key in stat:
        
        if stat[key] % 2 == 1:
            res.append(int(key))
    res.sort()
    result = ''
    for num in res:
        result += ' '
        result += str(num)
        
    ofile.write('Case #'+str(case+1)+':'+result+'\n')

ofile.close()