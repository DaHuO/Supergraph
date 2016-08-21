inputfile = "B-Large.in"
#inputfile = "sample.txt"
fin = open(inputfile, 'r')
fou = open('out.txt', 'w')

T = fin.readline()

for tc in xrange(int(T)):
    st = fin.readline()    
    flip = 0
    flag = st[0]
    for s in st:
        if s != '+' and s != '-':
            break
        
        if s != flag:
            flip += 1
            flag = s
    if flag == '-':
        flip += 1
    fou.write('Case #' + str(tc + 1) + ': ' + str(flip) + '\n')
    

fou.close()
fin.close()
