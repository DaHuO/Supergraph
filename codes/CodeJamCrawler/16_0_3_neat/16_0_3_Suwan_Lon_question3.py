def binlen(num, length):
    returnstr = bin(num)[2:]
    while len(returnstr) < length:
        returnstr = '0' + returnstr
    return returnstr


fin = open("C-large.in.txt", "r")
fout = open("C-large.out", "w")
cases = int(fin.readline())
for case in range(cases):
    fout.write("Case #{0}:\n".format(case + 1))
    inputstrs = fin.readline().split()
    coinlen = int(inputstrs[0])
    coinnum = int(inputstrs[1])
    fillinglen = coinlen // 2 - 2
    if coinlen % 2 != 0:
        mid = '101'
    else:
        mid = '11'
    for coinindx in range(coinnum):
        filling = binlen(coinindx, fillinglen)
        coin = '1' + filling + mid + filling + '1'
        divstr = '1' + filling + '1'
        writestr = coin
        for base in range(2, 11):
            writestr += ' ' + str(int(divstr, base))
        fout.write(writestr + "\n")
        
