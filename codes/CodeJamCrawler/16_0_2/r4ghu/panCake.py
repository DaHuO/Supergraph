input = open('input.txt','r')
print 'Name of the file:', input.name

results = []
T = int(input.readline())

for t in range(T):
    
    n = list(input.readline().strip())
    n.append('+')
    count = 0
    print n
    for i in range(len(n)-1):
        if n[i]=='-' and n[i+1]=='+':
            count+=1
            n[i]='+'
        if n[i]=='+' and n[i+1]=='-':
            count+=1
    results.append(str(count))



input.close()
print len(results),results
out = open('out.txt','w')
for i in range(len(results)):
    out.write('Case #'+str(i+1)+': '+results[i]+'\n')

