
f = open('C:\\Users\\Ton\\Desktop\\ggcj\\Round1A2016\\A\\A-large.in','rb')
fo = open('C:\\Users\\Ton\\Desktop\\ggcj\\Round1A2016\\A\\A-large.out','wb')
T = int(f.readline())
for tt in range(1,T+1):
    line = f.readline().strip()
    s = ''+line[0]
    line = line[1:]
    for c in line:
        if ord(c) >= ord(s[0]):
            s = c+s
        else:
            s = s+c
    print 'Case #{0}: {1}'.format(tt,s)
    fo.write('Case #{0}: {1}\n'.format(tt,s))
    
f.close()
fo.close()