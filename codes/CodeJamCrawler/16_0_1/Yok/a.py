'''
Created on Aug 30, 2009

@author: jirasak
'''

def process(number):
    alist = []
    while number > 0:
        alist.append(number % 10)
        number /= 10
    return alist

def proc_case(anum):
    aset = set()
    for i in range(1, 1000):
        aset = aset.union(process(anum * i))
        if len(aset) == 10:
            return i * anum
    return 'INSOMNIA'

if __name__ == '__main__':
    afile = file('A-large.in.txt')
    aread = afile.readlines()
    afile.close()
    
    aread = [x.strip() for x in aread]
    numcase = int(aread[0])
    
    cline = 1
    for casenum in range(1, numcase + 1):
        aline = aread[cline]
        anum = int(aline)
        cline += 1
        print 'Case #%d: %s' % (casenum, proc_case(anum))