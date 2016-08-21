inF = open('A-Large.in-2.txt','r')
ouF = open('MaryamQAL.out','w')
t = int(inF.readline())
for i in xrange(t):
    word = inF.readline().strip()
    res = word[0]
    for l in word[1:]:
        if l < res[0]:
            res = res + l
        else:
            res = l + res
    ouF.write('Case #' + str(i + 1) + ': ' + res+'\n')
