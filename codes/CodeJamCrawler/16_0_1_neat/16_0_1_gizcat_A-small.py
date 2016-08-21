import sys


# In[1]:

def getDigits(n):
    d = []
    while n>=10:
        d.append(n%10) 
        n /= 10
    d.append(n)
    return list(set(d))


t = int(sys.stdin.readline())
for _ in xrange(t):
    num = int(sys.stdin.readline())
    n = num
    digits = range(0,10)
    count = 1
    if n == 0:
        print 'Case #' + str(_+1) + ': '+ 'INSOMNIA'
        continue
    while len(digits) > 0:
        n = num * count
        d = getDigits(n)
        for i in d:
            if i in digits: digits.remove(i)
        count+=1
    print 'Case #' + str(_+1) + ': '+ str(n)

