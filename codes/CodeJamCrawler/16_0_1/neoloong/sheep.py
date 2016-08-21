in1 = open('sheep.in')
out1 = open('sheep.out', 'w')


n = int(in1.readline())

for i in range(0, n):
    num = int(in1.readline())
    if num == 0:
        out1.write("Case #%d: INSOMNIA\n" %(i+1))
        continue
    
    f = [0,0,0,0,0,0,0,0,0,0];
    len = 0;
    
    
    
    acc = 0;
    while len<10:
        acc += num
        temp = acc
        while temp>0:
            k = temp%10
            if f[k] == 0:
                f[k]=1
                len += 1
            temp /= 10
        
        
    out1.write("Case #%d: %d\n" %(i+1, acc))

in1.close();
out1.close();
    


