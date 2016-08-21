f = open('d.in','r')
o = open('d.out','w')

f.readline()
c = 0
for line in f:
    c += 1
    o.write("Case #" +str(c) + ":")
    K, C, S = line.split()
    K, C, S = int(K), int(C), int(S)
    for i in range (1, K+1):
        o.write(' ' + str(i))
    o.write('\n')
f.close()
o.close()
