import os.path
import re


with open('C:\Users\santosh\PycharmProjects\GoogleCodeJam\B-large.in') as f:
    content = f.readlines()

f1=open('C:\Users\santosh\PycharmProjects\GoogleCodeJam\outputPancake.txt', 'w+')

tEstCases = int(content[0])

for cases in range(1, tEstCases+1):

    pAncakes = content[cases]
    pAncakesS=pAncakes.rstrip('\n')
    #print pAncakesS

    LastCake = pAncakes[len(pAncakesS)-1]

    #print LastCake

    if LastCake is '-':
        FinalAdd=1
    else:
        FinalAdd=0

    seperated = [m.group() for m in re.finditer(r'(.)\1*', pAncakes)]

    minFlips = len(seperated)+FinalAdd-1

    #print 'Case #'+str(cases)+': '+str(minFlips)+'\n'
    f1.write('Case #'+str(cases)+': '+str(minFlips)+'\n')


f1.close()