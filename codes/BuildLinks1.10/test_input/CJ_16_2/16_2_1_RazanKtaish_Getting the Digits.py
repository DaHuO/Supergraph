output=[]
sr={'Z':'ZERO','W':'TWO','U':'FOUR','X':'SIX','G':'EIGHT'}
sr_num={'Z':0,'W':2,'U':4,'X':6,'G':8}
odd_number={'O':'ONE','H':'THREE','F':'FIVE','S':'SEVEN'}
number={'O':1,'H':3, 'F':5, 'S':7}
nine={'NINE':9}
def  find_num(string,num):
    for e in num :
        if e not in string :
            return False
    return True
def remove_num(string,num):
    for e in num :
        string.remove(e)
    return string

t=int(raw_input())
for ao in xrange(t):
    s=raw_input().strip()
    s=list(s)
    
    h=[]
    for w in sr :
        while find_num(s,sr[w]):
            s=remove_num(s,sr[w])
            h.append(str(sr_num[w]))
    
    for w in odd_number :
        while find_num(s,odd_number[w]):
            s=remove_num(s,odd_number[w])
            h.append(str(number[w]))
    while s:
        remove_num(s,'NINE')
        h.append(str(9))
                   
    h.sort()
    
    output.append(''.join(h))


for i in xrange(len(output)):
    print 'Case #'+str(i+1)+': '+output[i]


    
            
        
    
