l = []
with open('A-large.in') as f:
    for line in f:
        l.append(line.splitlines())
f = open('output2large.txt', 'w')
y = int(l[0][0])
for j in range(y):
    s = l[j+1][0]
    ans = ''
    while(len(s) > 0):
        if 'Z' in s:
            ans += '0'
            s = s.replace('Z', "", 1)
            s = s.replace('E', "", 1)
            s = s.replace('R', "", 1)
            s = s.replace('O', "", 1)
        elif 'W' in s:
            ans += '2'
            s = s.replace('T', '', 1)
            s = s.replace('W', '', 1)
            s = s.replace('O', '', 1)
        elif 'U' in s:
            ans += '4'
            s = s.replace('F', '', 1)
            s = s.replace('O', '', 1)
            s = s.replace('U', '', 1)
            s = s.replace('R', '', 1)
        elif 'X' in s:
            ans += '6'
            s = s.replace('S', '', 1)
            s = s.replace('I', '', 1)
            s = s.replace('X', '', 1)
        elif 'G' in s:
            s = s.replace('E', '', 1)
            s = s.replace('I', '', 1)
            s = s.replace('G', '', 1)
            s = s.replace('H', '', 1)
            s = s.replace('T', '', 1)
            ans += '8'
        elif 'F' in s:
            s = s.replace('F', '', 1)
            s = s.replace('I', '', 1)
            s = s.replace('V', '', 1)
            s = s.replace('E', '', 1)
            ans += '5'
        elif 'V' in s:
            s = s.replace('S', '', 1)
            s = s.replace('E', '', 1)
            s = s.replace('V', '', 1)
            s = s.replace('E', '', 1)
            s = s.replace('N', '', 1)
            ans += '7'
        elif 'T' in s:
            s = s.replace('T', '', 1)
            s = s.replace('H', '', 1)
            s = s.replace('R', '', 1)
            s = s.replace('E', '', 1)
            s = s.replace('E', '', 1)
            ans += '3'
        elif 'O' in s:
            s = s.replace('O', '', 1)
            s =  s.replace('N', '', 1)
            s = s.replace('E', '', 1)
            ans += '1'
        elif 'N' in s:
            s = s.replace('N', '', 1)
            s = s.replace('I', '', 1)
            s = s.replace('N', '', 1)
            s = s.replace('E', '', 1)
            ans += '9'
    f.write('Case #' + str(j+1)+': ')
        
    f.write(''.join(sorted(ans)))
    f.write('\n')
f.close()
