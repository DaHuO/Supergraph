

#Read python file

#infl = open('file.in','r+')
#infl = open('A-small-attempt0.in','r+')
infl = open('A-large.in','r+')
#outfl = open('Asmall.out','w')
outfl = open('Alarge.out','w')

cN = int(infl.readline())

for case in range(1,cN+1):
    out=""
    line1 = infl.readline()
    c1=line1[:1]
    line2 = line1[1:]
    out = out + c1
    for c in line2:
        fi = out[:1]
        lf = out[-1:]
        if (c>=fi):
            out = c + out
        else:
            out = out + c
    result ="Case #{}: {}".format(case,out)
    print(result)
    outfl.write(result)


infl.close()
outfl.close()