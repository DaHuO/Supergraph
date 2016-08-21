f = open('E:\\Code Jam 2016\\Last Word\\A-large.txt', mode = 'r')
fo = open('E:\\Code Jam 2016\\Last Word\\out.txt', mode = 'w')

testCases = int(f.readline())
output = ''
for case in range(1,testCases+1):
    s = list(f.readline())
    if(s[len(s)-1]=='\n'):
        s.remove('\n')
    first = s[0]
    word = [first]
    for i in range(1,len(s)):
        if (ord(s[i])>=ord(first)):
            word = [s[i]]+word
            first = s[i]
        else:
            word.append(s[i])
    output =  output+'Case #'+str(case)+': '+''.join(str(e) for e in word)+'\n'
fo.writelines(output)
print 'done'
