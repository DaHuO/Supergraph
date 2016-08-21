f = open('TheLastWordin.txt','r')
t = int(f.readline())
g = open('TheLastWordout.txt','w').close()
g = open('TheLastWordout.txt','a')
alphaDictionary = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
for i in xrange(1, t+1):
    n = i
    answerString = ""
    S = str(f.readline())
    answerString = S[0]
    for i in range(len(S)):
        character = S[i]
        #print answerString
        if(character=='\n'):
            continue
        if(i==0):
            continue
        else:
            if(alphaDictionary[character]>=alphaDictionary[answerString[0]]):
                answerString = character+answerString
            else:
                answerString = answerString+character
        
    g.write( "Case #{}: {}\n".format(n, answerString))
g.close()
f.close()