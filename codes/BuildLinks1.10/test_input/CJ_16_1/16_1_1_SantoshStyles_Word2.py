with open('C:\Users\santosh\PycharmProjects\GoogleCodeJam\A-large.in') as f:
    content = f.readlines()

f1=open('C:\Users\santosh\PycharmProjects\GoogleCodeJam\outputWord.txt', 'w+')

tEstCases = int(content[0])
#print tEstCases

s = "ZXCASDQWE"
m = list(s)
l = len(m)
#print l
#print len(s)
#print s[1]
word = s[0]

#print max(s)

for cases in range(1, tEstCases+1):
    original = content[cases]
    word = original[0]
    #print word
    l= len(original)
    for x in xrange(1, l):
        if max(original[x],word[0])== original[x]:
            word = original[x]+word
        elif max(original[x],word[0])== word[0]:
            word = word + original[x]
        else:
            print "error main for loop"

    f1.write('Case #'+str(cases)+': '+word)
    print word


