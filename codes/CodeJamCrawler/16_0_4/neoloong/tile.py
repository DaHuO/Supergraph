in1 = open('tile.in')
out1 = open('tile.out', 'w')


n = int(in1.readline())

for i in range(0, n):
    str1,str2,str3 = in1.readline().split()
    K = int(str1)
    C = int(str2)
    S = int(str3)
    if S<K: 
        out1.write("Case #%d: IMPOSSIBLE\n" %(i+1))
        continue
    
    out1.write("Case #%d:" %(i+1))
    for j in range(1,K+1):
        out1.write(" %d" %(K**(C-1)*j))
    out1.write('\n')
    

in1.close();
out1.close();
