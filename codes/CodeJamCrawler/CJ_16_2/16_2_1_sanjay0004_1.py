t = int(raw_input())

for a in range(t):
    s = raw_input()
    d = {0 : 0 , 1 : 0 , 2 : 0 , 3 : 0 , 4 : 0 , 5 : 0 , 6 : 0 , 7 : 0 , 8 : 0 , 9 : 0 , 'N' : 0, 'O' : 0, 'V' : 0, 'F' : 0 , 'H' : 0}

    for i in range(len(s)):
        if s[i] == 'Z' :
            d[0] = d[0] + 1
        elif s[i] == 'W':
            d[2] = d[2] + 1
        elif s[i] == 'U':
            d[4] = d[4] + 1
        elif s[i] == 'X':
            d[6] = d[6] + 1
        elif s[i] == 'G':
            d[8] = d[8] + 1
            
        elif s[i] == 'H':
            d['H'] = d['H'] + 1
            
        elif s[i] == 'N':
            d['N'] = d['N'] + 1
        elif s[i] == 'O':
            d['O'] = d['O'] + 1
            
        elif s[i] == 'V':
            d['V'] = d['V'] + 1
        elif s[i] == 'F':
            d['F'] = d['F'] + 1


    d[3] = d['H'] - d[8]
    d[1] = d['O'] - d[0] - d[2] - d[4]
    
    d[5] = d['F'] - d[4]
    d[7] = d['V'] - d[5]
    d[9] = (d['N'] - d[1] - d[7])/2
    sf = ''
    for b in range(10):
        sf = sf + str(b)*d[b]

    print "Case #%s: %s"  %(a+1 ,sf)
