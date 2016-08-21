d={}
n=''
number={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
t=input()
for _ in xrange(t):
    n=''
    for i in xrange(65,92):
        d[chr(i)]=0
    s=raw_input()
    for i in s:
        d[i]+=1
    
    
    if d['Z']>0:
        while d['Z']>0:
                d['Z']-=1
                d['E']-=1
                d['R']-=1
                d['O']-=1
                n+='0'
    if d['X']>0:
        while d['X']>0:
                d['S']-=1
                d['I']-=1
                d['X']-=1
                n+='6'
    if d['U']>0:
        while d['U']>0:
                d['F']-=1
                d['O']-=1
                d['U']-=1
                d['R']-=1
                n+='4'
    if d['W']>0:
        while d['W']>0:
                d['T']-=1
                d['W']-=1
                d['O']-=1
                n+='2'

    if d['G']>0:
        while d['G']>0:
                d['E']-=1
                d['I']-=1
                d['G']-=1
                d['H']-=1
                d['T']-=1
                n+='8'
        
    if d['S']>0 and d['V']>0:
        while min(d['S'],d['V'])>0:
                d['S']-=1
                d['E']-=1
                d['V']-=1
                d['E']-=1
                d['N']-=1
                n+='7'
                
    if d['F']>0 and d['V']>0:
        while min(d['F'],d['V'])>0:
                d['F']-=1
                d['I']-=1
                d['V']-=1
                d['E']-=1
                n+='5'
                
    if d['O']>0 and d['E']>0:
        while min(d['O'],d['E'])>0:
                d['O']-=1
                d['N']-=1
                d['E']-=1
                n+='1'

    if d['N']>0 and d['E']>0:
        while min(d['N'],d['E'])>0:
                d['N']-=1
                d['I']-=1
                d['N']-=1
                d['E']-=1
                n+='9'
                
    if d['R']>0 and d['E']>0:
        while min(d['R'],d['E'])>0:
                d['T']-=1
                d['H']-=1
                d['R']-=1
                d['E']-=2
                n+='3'
    n=list(n)
    n.sort()
    print "Case #{}: {}".format( _+1, ''.join(n))

