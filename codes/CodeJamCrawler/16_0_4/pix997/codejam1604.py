t = input()
b = []
for i in range(t):
    a = raw_input().split(' ')
    a = int(a[0])
    b.append(a)
for i in range(t):
    print "Case #"+str(i+1)+":",
    for j in range(1,b[i]+1):
        print j,
    print ''
