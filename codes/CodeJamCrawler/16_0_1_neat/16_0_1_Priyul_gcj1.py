fin = open('A-large.in','r')
fout = open('op1.in','w')
T = int(fin.readline())
for i in range(0,T):
    N =int(fin.readline())
    if (N == 0 ):
        out = "case #" + str(i+1) + ": " + "INSOMNIA\n"
        fout.write(out)
        #print("INSOMNIA")
        continue
    digit = list()
    n = N
    count = 2
    while(len(digit) != 10) :
        str1 = str(n)
        for j in range(0,len(str1)):
            if str1[j] not in digit :
                digit.append(str1[j])
        if(len(digit)!=10):
            n = count * N
            count = count + 1
    out = "case #" + str(i+1) + ": " + str(n) + "\n"
    fout.write(out)
    #print(n)
    #print(digit)
fin.close()
fout.close()
