'''
Created on Aug 30, 2009

@author: jirasak
'''

def proc_case(aline):
    current = None
    cnt = 0
    i = 0
    for a in aline:
        if current is None:
            current = a
        elif current == a:
            pass
        else:
            current = a
            cnt += 1
        
        if i == len(aline) - 1:
            if current == '-':
                cnt += 1
        i += 1
    return cnt

if __name__ == '__main__':
    afile = file('B-large.in.txt')
    aread = afile.readlines()
    afile.close()
    
    aread = [x.strip() for x in aread]
    numcase = int(aread[0])
    
    cline = 1
    for casenum in range(1, numcase + 1):
        aline = aread[cline]
        aline = list(aline)
        cline += 1
        print 'Case #%d: %s' % (casenum, proc_case(aline))