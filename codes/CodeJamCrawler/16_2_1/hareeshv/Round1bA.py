l = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
def contains(small, big):
    for i in xrange(len(big)-len(small)+1):
        for j in xrange(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False

for i  in range(input()):
    res = []
    r = list(raw_input())
    d = dict()
    for k in r:
        if k in d:
            d[k] += 1
        else:
            d[k] = 1
    print "Case #"+str(i+1)+":",
    temp = r.count('Z')
    if temp:
        res += '0' * temp
        d['Z'] -= temp;d['E'] -= temp;d['R'] -= temp;d['O'] -= temp

    temp = r.count('W')
    if temp:
        res += '2' * temp
        d['T'] -= temp;d['W'] -= temp;d['O'] -= temp

    temp = r.count('U')
    if temp:
        res += '4' * temp
        d['F'] -= temp;d['O'] -= temp;d['U'] -= temp;d['R'] -= temp

    temp = r.count('X')
    if temp:
        res += '6' * temp
        d['S'] -= temp;d['I'] -= temp;d['X'] -= temp

    temp = r.count('G')
    if temp:
        res += '8' * temp
        d['E'] -= temp;d['I'] -= temp;d['G'] -= temp;d['H'] -= temp;d['T'] -= temp


    if 'T' in d and d['T']:
        temp = d['T']
        res += '3' * temp
        d['T'] -= temp;d['H'] -= temp;d['R'] -= temp;d['E'] -= temp;d['E'] -= temp


    if 'F' in d and d['F']:
        temp = d['F']
        res += '5' * temp
        d['F'] -= temp;d['I'] -= temp;d['V'] -= temp;d['E'] -= temp


    if 'V' in d and d['V']:
        temp = d['V']
        res += '7' * temp
        d['S'] -= temp;d['E'] -= temp;d['V'] -= temp;d['E'] -= temp;d['N'] -= temp


    if 'I' in d and d['I']:
        temp = d['I']
        res += '9' * temp
        d['N'] -= temp;d['I'] -= temp;d['N'] -= temp;d['E'] -= temp;

    if 'N' in d and d['N']:
        temp = d['N']
        res += '1' * temp

    print (''.join(sorted(res)))
