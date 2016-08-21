# Read it
fin_s = "A-large.in"
fou_s = fin_s + '.out'
fin = open(fin_s, 'r')
fou = open(fou_s, 'w')

# Solve it
T = int(fin.readline())

for t in range(T):
    input_str = fin.readline().strip()
    #print(str)
    alph_cnt = {'E':0,'F':0, 'G':0, 'H':0, 'I':0, 'N':0, 'O':0, 'R':0, 'S':0,'T':0, 'U':0, 'V':0, 'W':0,'X':0, 'Z':0}
    
    numbers = []
    
    for i in range(len(input_str)):
        #print(str[i])
        alph_cnt[input_str[i]] = alph_cnt[input_str[i]] + 1
    #print(alph_cnt)
    
    for i in range(alph_cnt['W']):
        numbers.append(2)
    alph_cnt['T'] = alph_cnt['T'] - alph_cnt['W']
    alph_cnt['O'] = alph_cnt['O'] - alph_cnt['W']
    alph_cnt['W'] = 0
    
    for i in range(alph_cnt['Z']):
        numbers.append(0)
    alph_cnt['E'] = alph_cnt['E'] - alph_cnt['Z']
    alph_cnt['R'] = alph_cnt['R'] - alph_cnt['Z']
    alph_cnt['O'] = alph_cnt['O'] - alph_cnt['Z']
    alph_cnt['Z'] = 0
    
    for i in range(alph_cnt['X']):
        numbers.append(6)
    alph_cnt['S'] = alph_cnt['S'] - alph_cnt['X']
    alph_cnt['I'] = alph_cnt['I'] - alph_cnt['X']
    alph_cnt['X'] = 0
    
    for i in range(alph_cnt['G']):
        numbers.append(8)
    alph_cnt['E'] = alph_cnt['E'] - alph_cnt['G']
    alph_cnt['I'] = alph_cnt['I'] - alph_cnt['G']
    alph_cnt['H'] = alph_cnt['H'] - alph_cnt['G']
    alph_cnt['T'] = alph_cnt['T'] - alph_cnt['G']
    alph_cnt['G'] = 0
    
    for i in range(alph_cnt['H']):
        numbers.append(3)
    alph_cnt['T'] = alph_cnt['T'] - alph_cnt['H']
    alph_cnt['R'] = alph_cnt['R'] - alph_cnt['H']
    alph_cnt['E'] = alph_cnt['E'] - alph_cnt['H']
    alph_cnt['E'] = alph_cnt['E'] - alph_cnt['H']
    alph_cnt['H'] = 0
    
    for i in range(alph_cnt['R']):
        numbers.append(4)
    alph_cnt['F'] = alph_cnt['F'] - alph_cnt['R']
    alph_cnt['O'] = alph_cnt['O'] - alph_cnt['R']
    alph_cnt['U'] = alph_cnt['U'] - alph_cnt['R']
    alph_cnt['R'] = 0
    
    for i in range(alph_cnt['O']):
        numbers.append(1)
    alph_cnt['N'] = alph_cnt['N'] - alph_cnt['O']
    alph_cnt['E'] = alph_cnt['E'] - alph_cnt['O']
    alph_cnt['O'] = 0
    
    for i in range(alph_cnt['F']):
        numbers.append(5)
    alph_cnt['I'] = alph_cnt['I'] - alph_cnt['F']
    alph_cnt['V'] = alph_cnt['V'] - alph_cnt['F']
    alph_cnt['E'] = alph_cnt['E'] - alph_cnt['F']
    alph_cnt['F'] = 0
    
    for i in range(alph_cnt['V']):
        numbers.append(7)
    alph_cnt['S'] = alph_cnt['S'] - alph_cnt['V']
    alph_cnt['E'] = alph_cnt['E'] - alph_cnt['V']
    alph_cnt['E'] = alph_cnt['E'] - alph_cnt['V']
    alph_cnt['N'] = alph_cnt['N'] - alph_cnt['V']
    alph_cnt['V'] = 0
    
    for i in range(int(alph_cnt['N']/2)):
        numbers.append(9)
    alph_cnt['I'] = alph_cnt['I'] - int(alph_cnt['N']/2)
    alph_cnt['E'] = alph_cnt['E'] - int(alph_cnt['N']/2)
    alph_cnt['N'] = 0
    
    print(alph_cnt)
    
    pn = sorted(numbers)
    
    # Write routines
    fou.write('Case #' + str(t + 1) + ': ')
    for i in range(len(pn)):
        fou.write(str(pn[i]))
    fou.write('\n')
    
# Finish it
fin.close()
fou.close()