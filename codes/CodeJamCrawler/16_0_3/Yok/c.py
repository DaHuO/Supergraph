'''
Created on Aug 30, 2009

@author: jirasak
'''

def is_prime(n):
    if n == 2 or n == 3: 
        return True, None
    if n < 2 or n % 2 == 0: 
        return False, 2
    if n < 9: return True, None
    if n % 3 == 0: return False, 3
    r = int(n ** 0.5)
    f = 5
    while f <= r:
#         print '\t',f
        if n % f == 0: return False, f
        if n % (f+2) == 0: return False, (f+2)
        f +=6
    return True, None

def jam_coin(n, j):
    counting_j = 0
    for i in range(2 ** (n-2)):
        abin = bin(i)[2:]
        alen = len(abin)
        num = '1%s1' % ( ('0' * ((n-2) - alen)) + abin)
        has_prime = False
        output = []
        for i in range(2,11):
            anum = int(num, i)
            ip, divisor = is_prime(anum)
            if ip:
                has_prime = True
                break
            else:
                output.append(divisor)
        if not has_prime:
            print num, ' '.join([str(x) for x in output])
            counting_j += 1
            if counting_j == j:
                return
        else:
            pass
    return ''

if __name__ == '__main__':
    afile = file('c.in')
    aread = afile.readlines()
    afile.close()
    
    aread = [x.strip() for x in aread]
    numcase = int(aread[0])
    
    cline = 1
    for casenum in range(1, numcase + 1):
        aline = aread[cline]
        aline = [int(x) for x in aline.split(' ')]
        cline += 1
        print 'Case #%d:' % (casenum)
        jam_coin(aline[0], aline[1])