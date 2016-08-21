from sets import Set 
filein = open('B-large.in', 'r')
fileout = open('B-large.out', 'w')
 
T = int(filein.readline())
for t in range(T):
    fileout.write('Case #%d: ' % (t + 1))
    s = filein.readline()
    s = s[::-1]
    rst = 0
    for idx in range(len(s)):
        if s[idx] == '-':
            if rst%2 == 0:
                rst += 1
        else:
            if rst%2 == 1:
                rst += 1
    fileout.write(str(rst)+"\n")

            


 
filein.close()
fileout.close()