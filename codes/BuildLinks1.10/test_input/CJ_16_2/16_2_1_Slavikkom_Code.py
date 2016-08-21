file = open('C:\\Users\\V\\Downloads\\a1.in','r')
f = file.read()
result=f.split("\n")
n = int(result[0])
i = 0
file.close()
print result
del result[0]
file = open('C:\\Users\\V\\Downloads\\Submit.txt','w')
for s in result:
    m = len(s)
    answer = []
    z = s.count('Z')
    w = s.count('W')
    g = s.count('G')
    x = s.count('X')
    u = s.count('U')
    o = s.count('O')
    e = s.count('E')
    n = s.count('N')
    v = s.count('V')
    r = s.count('R')
    i = s.count('I')
    ss = s.count('S')
    sev = ss - x
    thr = r - z - u
    five = v - sev
    one = o - z - w - u
    nine = i - five - x - g
    for i in range(z):
        answer.append(0)
    for i in range(w):
        answer.append(2)    
    for i in range(x):
        answer.append(6)
    for i in range(u):
        answer.append(4)    
    for i in range(g):
        answer.append(8)    
    for i in range(thr):
        answer.append(3)  
    for i in range(sev):
        answer.append(7)
    for i in range(five):
        answer.append(5)
    for i in range(one):
        answer.append(1)  
    for i in range(nine):
        answer.append(9)    
        
    answer.sort()
    o = ""
    for k in answer:
        o = o + str(k)
    ans = ''.join(set(str(answer)))
    file.write("Case #" + str(i + 1) + ": "  + o + "\n")
    print "Case #" + str(i + 1) + ": "+ o + "\n"
    i = i + 1
print result
file.close()
#file = open('C:\\Users\\V\\Downloads\\Submit.txt','w')

print result