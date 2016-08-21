input = open('input.txt','r')
print 'Name of the file:', input.name

results = []
T = int(input.readline())

list = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
for t in xrange(T):
    s = input.readline().strip()
    dic = {}
    for i in s:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
    # Check for zeros
    if ('Z' in dic.keys()) and ('E' in dic.keys()) and ('R' in dic.keys()) and ('O' in dic.keys()):
        num0 = ('0'*dic['Z'])
        dic['E'] -= dic['Z']
        dic['R'] -= dic['Z']
        dic['O'] -= dic['Z']
    else:
        num0 = ''
    if ('W' in dic.keys()) and ('T' in dic.keys()) and ('O' in dic.keys()):
        num2 = ('2'*dic['W'])
        dic['T'] -= dic['W']
        dic['O'] -= dic['W']
    else: num2 = ''
    if ('U' in dic.keys()) and ('F' in dic.keys()) and ('R' in dic.keys()) and ('O' in dic.keys()):
        num4 = ('4'*dic['U'])
        dic['F'] -= dic['U']
        dic['O'] -= dic['U']
        dic['R'] -= dic['U']
    else: num4 = ''
    if ('O' in dic.keys()) and ('E' in dic.keys()) and ('N' in dic.keys()):
        num1 = ('1'*dic['O'])
        dic['N'] -= dic['O']
        dic['E'] -= dic['O']
    else: num1 = ''
    if ('F' in dic.keys()) and ('E' in dic.keys()) and ('I' in dic.keys()) and ('V' in dic.keys()):
        num5 = ('5'*dic['F'])
        dic['I'] -= dic['F']
        dic['V'] -= dic['F']
        dic['E'] -= dic['F']
    else: num5 = ''
    if ('X' in dic.keys()) and ('S' in dic.keys()) and ('I' in dic.keys()):
        num6 = ('6'*dic['X'])
        dic['S'] -= dic['X']
        dic['I'] -= dic['X']
    else: num6 = ''
    if ('S' in dic.keys()) and ('E' in dic.keys()) and ('V' in dic.keys()) and ('N' in dic.keys()):
        num7 = ('7'*dic['S'])
        dic['E'] -= 2*dic['S']
        dic['V'] -= dic['S']
        dic['N'] -= dic['S']
    else: num7 = ''
    if ('G' in dic.keys()) and ('E' in dic.keys()) and ('I' in dic.keys()) and ('H' in dic.keys()) and ('T' in dic.keys()):
        num8 = ('8'*dic['G'])
        dic['E'] -= dic['G']
        dic['I'] -= dic['G']
        dic['H'] -= dic['G']
        dic['T'] -= dic['G']
    else: num8 = ''
    if ('I' in dic.keys()) and ('E' in dic.keys()) and ('N' in dic.keys()):
        num9 = ('9'*dic['I'])
        dic['N'] -= 2*dic['I']
        dic['E'] -= dic['I']
    else: num9 = ''
    if ('H' in dic.keys()) and ('E' in dic.keys()) and ('R' in dic.keys()) and ('T' in dic.keys()):
        num3 = ('3'*dic['H'])
        dic['E'] -= 2*dic['H']
        dic['R'] -= dic['H']
        
        dic['T'] -= dic['H']
    else: num3 = ''
    num = num0+num1+num2+num3+num4+num5+num6+num7+num8+num9
    results.append(num)


input.close()
print len(results),results
out = open('out.txt','w')
for i in range(len(results)):
    out.write('Case #'+str(i+1)+': '+results[i]+'\n')

