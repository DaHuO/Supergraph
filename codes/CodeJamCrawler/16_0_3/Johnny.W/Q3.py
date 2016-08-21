import math 

def is_prime(num):
    if num == 0 or num == 1:
        return (False, None)
    for x in range(2, int(math.sqrt(num) + 1)):
        if num % x == 0:
            return (False, x)
    else:
        return (True, None)

def solve(n,j):
    resList = ''
    c = 0
    begin = '0'*(n-2)
    end = '1'*(n-2)
    bases = range(2,11)
    for i in xrange(int(begin,2), int(end,2)+1):
        valid = True
        fList = []
        i += 2**(n-2)
        s = str(bin(i))[2:]+'1'
        # print 'string = ' + s
        for base in bases:
            num = int(s, base = base)
            res = is_prime(num)
            if not res[0]:
                fList.append(res[1])
            else: 
                valid = False
                # print 'base', base,'num',num,'isPrime'
                break
        if valid:
            c += 1
            resList += s
            resList += ' '
            resList += ' '.join(str(x) for x in fList)
            resList += '\n'
            if c == j:
                return resList
print 'Case #1:'
print solve(16,50)

