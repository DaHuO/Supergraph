
'''
Created on Apr 9, 2016

@author: Ibrahim
'''

def func (string):

    result = ''+string[0]
    for i in xrange(1,len(string)):
        letter = string[i]
        if letter >= result[0]:
            result = letter + result
        else:
            result = result + letter
            
    return result
'''
Driver code
'''
f = open('A-large (2).in','r')
outf = open ('large.out','w')
T = int(f.readline())

for i in xrange(0,T):
    string = f.readline().rstrip()
    answer = func(string)
    print 'Case #'+str(i+1)+': '+str(answer)
    outf.write('Case #'+str(i+1)+': '+str(answer)+'\n')
