import sys

caseN=int(input())
for n in range(1,caseN+1):
    orgstr=input()

    dic={}
    for i in range(0,len(orgstr)):
        if orgstr[i] not in dic:
            dic[ orgstr[i] ] = 0
        dic[ orgstr[i] ] += 1
    #print(dic)#chk dic
    
    digits=[]
        
    if 'Z' in dic:
        cnt=dic['Z']
        dic['Z'] -= cnt
        dic['E'] -= cnt
        dic['R'] -= cnt
        dic['O'] -= cnt
        for x in range(0,cnt):
            digits.append('0')

    if 'W' in dic:
        cnt=dic['W']
        dic['T'] -= cnt
        dic['W'] -= cnt
        dic['O'] -= cnt
        for x in range(0,cnt):
            digits.append('2')
            
    if 'U' in dic:
        cnt=dic['U']
        dic['F'] -= cnt
        dic['O'] -= cnt
        dic['U'] -= cnt
        dic['R'] -= cnt
        for x in range(0,cnt):
            digits.append('4')

    if 'X' in dic:
        cnt=dic['X']
        dic['S'] -= cnt
        dic['I'] -= cnt
        dic['X'] -= cnt
        for x in range(0,cnt):
            digits.append('6')

    if 'G' in dic:
        cnt=dic['G']
        dic['E'] -= cnt
        dic['I'] -= cnt
        dic['G'] -= cnt
        dic['H'] -= cnt
        dic['T'] -= cnt
        for x in range(0,cnt):
            digits.append('8')
            
    if 'T' in dic:
        if not(dic['T']==0):
            cnt=dic['T']
            dic['T'] -= cnt
            dic['H'] -= cnt
            dic['R'] -= cnt
            dic['E'] -= cnt*2
            for x in range(0,cnt):
                digits.append('3')

    if 'F' in dic:
        if not(dic['F']==0):
            cnt=dic['F']
            dic['F'] -= cnt
            dic['I'] -= cnt
            dic['V'] -= cnt
            dic['E'] -= cnt
            for x in range(0,cnt):
                digits.append('5')

    if 'S' in dic:
        if not(dic['S']==0):
            cnt=dic['S']
            dic['S'] -= cnt
            dic['E'] -= cnt*2
            dic['V'] -= cnt
            dic['N'] -= cnt
            for x in range(0,cnt):
                digits.append('7')

    if 'O' in dic:
        if not(dic['O']==0):
            cnt=dic['O']
            dic['O'] -= cnt
            dic['N'] -= cnt
            dic['E'] -= cnt
            for x in range(0,cnt):
                digits.append('1')

    if 'I' in dic:
        if not(dic['I']==0):
            cnt=dic['I']
            dic['N'] -= cnt*2
            dic['I'] -= cnt
            dic['E'] -= cnt
            for x in range(0,cnt):
                digits.append('9')

    digits.sort()
    answer="".join(digits)
    print("Case #%d: %s"%(n,answer))
        
