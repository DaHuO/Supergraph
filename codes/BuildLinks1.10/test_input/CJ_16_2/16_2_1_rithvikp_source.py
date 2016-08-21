num=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN']
myfile = open('ip')
ansfile=open('ans','a')
##def check(n,s):
##    count=0
##    if n=='ZERO':
##        if 'Z' not in s:
##            return 0
##        else:
##            return n
##    elif n=='TWO':
##        if 'W' not in s:
##            return 0
##        else:
##            return n
##    elif n=='FOUR':
##        if 'U' not in s:
##            return 0
##        else:
##            return n
##    elif n=='SIX':
##        if 'X' not in s:
##            return 0
##        else:
##            return n
##    elif n=='EIGHT':
##        if 'G' not in s:
##            return 0
##        else:
##            return n
##    else:
##        for i in n:
##            if i in s and s.count(i)>=n.count(i):
##                count+=1
##        if count==len(n):
##            return n
##        else:
##            return 0
def rem(n,s):
    for i in n:
        #print(i)
        index=s.index(i)
        s=s[:index]+s[index+1:]
    return s
for i in range(int(myfile.readline())):
    s=str(myfile.readline())
    s=s.replace('\n','')
    op=[]
    t=0
    while s!='':
        if 'Z' in s:
            op.append('ZERO')
            s=rem('ZERO',s)
        elif 'W' in s:
            op.append('TWO')
            s=rem('TWO',s)
        elif 'X' in s:
            op.append('SIX')
            s=rem('SIX',s)
        elif 'U' in s:
            op.append('FOUR')
            s=rem('FOUR',s)
        elif 'G' in s:
            op.append('EIGHT')
            s=rem('EIGHT',s)
        elif 'S' in s:
            op.append('SEVEN')
            s=rem('SEVEN',s)
        elif 'R' in s:
            op.append('THREE')
            s=rem('THREE',s)
        elif 'V' in s:
            op.append('FIVE')
            s=rem('FIVE',s)
        elif 'I' in s:
            op.append('NINE')
            s=rem('NINE',s)
        else:
            op.append('ONE')
            s=rem('ONE',s)
        
    answer=''
    for j in op:
        if j=='ZERO':
            answer+='0'
        elif j=='ONE':
            answer+='1'
        elif j=='TWO':
            answer+='2'
        elif j=='THREE':
            answer+='3'
        elif j=='FOUR':
            answer+='4'
        elif j=='FIVE':
            answer+='5'
        elif j=='SIX':
            answer+='6'
        elif j=='SEVEN':
            answer+='7'
        elif j=='EIGHT':
            answer+='8'
        else:
            answer+='9'
    answer=sorted(answer)
    final=''
    for j in answer:
        final+=j
    final+='\n'
    ansfile.write('Case #'+str(i+1)+': '+final)
ansfile.close()
myfile.close()
