def digitize(inint,btest):
    instr = str(inint)
    for i in range(len(instr)):
        btest[int(instr[i])]=True
    return btest
filename='A-small-attempt0'
file_in = open(filename+'.in','r')
file_out = open(filename+'.out','w')
cases = int(file_in.readline())
print cases
for i in range(cases):
    btest=[False]*10
    n = int(file_in.readline())
    print n
    j=1
    btest = digitize(n,btest)
    while not all(btest):
        j = j + 1
        n1 = n*j
#         print n1
        if n1==n:
            break
        btest = digitize(n1,btest)

    print 'Case #'+str(i+1)+': '+str(n1)
    if n1==n:
        file_out.writelines('Case #%s: INSOMNIA\n'%(i+1))
    else:
        file_out.writelines('Case #%s: %d\n'%(i+1,n1))

file_in.close()
file_out.close()
