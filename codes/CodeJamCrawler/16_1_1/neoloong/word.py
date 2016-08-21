in1 = open('word.in')
out1 = open('word.out', 'w')


n = int(in1.readline())

for i in range(0, n):
    str = in1.readline()
    wd = str[0]
    for j in range(1,len(str)):
         if str[j]>=wd[0]:
             wd = str[j] + wd
         else:
             wd = wd + str[j]
    out1.write("Case #%d: %s" %(i+1,wd))
    
in1.close();
out1.close();