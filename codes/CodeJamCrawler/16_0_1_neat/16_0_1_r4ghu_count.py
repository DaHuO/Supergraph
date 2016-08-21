input = open('input.txt','r')
print 'Name of the file:', input.name

results = []
T = int(input.readline())

for t in range(T):
    dic = {}
    l = []
    n = int(input.readline())
    
    if n==0:
        results.append('INSOMNIA')
    for i in range(1,25*n):
        p = list(str(i*n))
        for j in p:
            if j not in dic.keys():
                dic[j]=1
        l = dic.keys()
        l.sort()
        if l==['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            results.append(str(i*n))
            break




input.close()
print len(results),results
out = open('out.txt','w')
for i in range(len(results)):
    out.write('Case #'+str(i+1)+': '+results[i]+'\n')

