in1 = open('pan.in')
out1 = open('pan.out', 'w')


n = int(in1.readline())

for i in range(0, n):
    str = in1.readline()
    flip = 0
    l = len(str)-1
    
    for j in range(0, l-1):
        if str[j] == str[j+1]: continue
        flip += 1
    if str[l-1] == '-': flip += 1
    
    out1.write("Case #%d: %d\n" %(i+1, flip))

in1.close();
out1.close();
