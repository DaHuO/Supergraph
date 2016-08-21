'''
Created on Aug 30, 2009

@author: jirasak
'''

def solve(k, c, s):
    if c == 1:
        return ' '.join([str(x) for x in range(1, k+1)])
    if k == 1:
        return 1
    output = []
    for i in range(k - 1):
        output.append((2 + i) + ((k ** (c-1)) * i))
    return ' '.join([str(x) for x in output])

if __name__ == '__main__':
    afile = file('D-small-attempt0.in.txt')
    aread = afile.readlines()
    afile.close()
    
    aread = [x.strip() for x in aread]
    numcase = int(aread[0])
    
    cline = 1
    for casenum in range(1, numcase + 1):
        aline = aread[cline]
        aline = [int(x) for x in aline.split(' ')]
        cline += 1
        print 'Case #%d: %s' % (casenum, solve(aline[0], aline[1], aline[2]))