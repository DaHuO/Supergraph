def transform(s, i, j, char):
    maxc, resi = 0, i-1
    k = i
    while k<=j:
        count = 0
        while k<=j and s[k] == char:
            count += 1
            k += 1
        if maxc < count:
            maxc = count
            resi = k
        while k<=j and s[k] != char:
            k+=1
    if char == '+':
        rev =''.join([ '-' if item=='+' else '+'  for item in s[i:resi]][::-1])
        return s[:i] + rev + s[resi:]
    else:
        rev = ''.join([ '-' if item=='+' else '+'  for item in s[resi-maxc:j+1]][::-1])
        return s[:resi-maxc] + rev + s[j+1:]


t = int(raw_input())
for index in xrange(1, t+1):
    s = raw_input()
    if len(s) == 0:
        print 'Case #{}: {}'.format(index, 0)
    count = 0
    i,j = 0, len(s)-1
    while i<=j and s[j] == '+':
        j-=1
    c=-1
    while i<=j:
        if c<0:
            if s[i] != '-':
                s = transform(s, i, j, '+')
                count += 1
            while i<=j and s[i] == '-':
                i+=1
            count += 1
        else:
            if s[j] != '+':
                s = transform(s, i, j, '-')
                count += 1
            while i<=j and s[j] == '+':
                j-=1
            count+=1
        c *= -1
    print 'Case #{}: {}'.format(index, count)



