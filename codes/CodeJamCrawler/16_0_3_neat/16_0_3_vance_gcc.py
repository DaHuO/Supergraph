def stoi(s, b):
    ret = 0
    for i in range(len(s)):
        ret = ret*b + int(s[i])
    return ret
def isprime(n):
    if n < 2:
        return n
    i = 2
    while i*i <= n:
        if n%i == 0:
            return i
        i += 1
    return n
def main():
    print 'Case #1:'
    n = 16
    j = 50
    for i in range(2**(n-2)):
        s = '{0:b}'.format(i)
        while len(s) < n-2:
            s = '0' + s
        s = '1' + s + '1'
        fs = []
        for b in range(2, 11):
            sn = stoi(s, b)
            f = isprime(sn)
            if f != sn:
                fs.append(str(f))
            else:
                break
        if len(fs) == 9:
            print s, ' '.join(fs)
            j -= 1
        if j == 0:
            break
        #print s, stoi(s, 2)

main()
