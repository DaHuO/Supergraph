def fermat(n):
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(2, n-1, n) == 1
found = 0

for i in range(0,2**14+1):
    bstring = '{0:014b}'.format(i)
    bstring = '1' + bstring + '1'
    isjamcoin = True
    intlist = []
    
    for j in range (2,11):
        test = int(bstring, j)
        if fermat(test):
            isjamcoin = False
            break
        k = 2
        while test % k != 0:
            k = k + 1
        intlist.append(k) 

    if isjamcoin:
        formatlist = ''
        for divisor in intlist:
            formatlist += str(divisor) + ' '
        found = found + 1

        print bstring + ' ' + formatlist

    if (found > 50):
        break

