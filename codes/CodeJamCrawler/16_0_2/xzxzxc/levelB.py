fName = 'B-large.in'
inpFile = open(fName)
outpFile = file('output'+fName[:7], 'w')


def repl(mystring):
    newstring = ''
    for char in mystring:
        if char == '+':
            newstring += '-'
        else:
            newstring +='+'
    return newstring

for T in xrange(int(inpFile.readline())):
    S = inpFile.readline()
    nom = 0
    while S.count('-') != 0:
        lastMin = S.rfind('-')
        npas = 0
        for char in S:
            if char == '+':
                npas += 1
            else:
                break
        if npas == 0:
            S = repl(S[:lastMin+1])[::-1]+S[lastMin+1:]
            nom += 1
        else:
            S = repl(S[:npas])[::-1]+S[npas:]
            S = repl(S[:lastMin+1])[::-1]+S[lastMin+1:]
            nom += 2
    outpFile.write('Case #'+str(T+1)+': '+str(nom)+'\n')


outpFile.close()
inpFile.close()