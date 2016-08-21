fin = open("A-large.in","r")
fout = open("op.in","w")

T = int(fin.readline())

for i in range(0,T):
    #print(i)
    S = fin.readline()
    S.rstrip('\n')
    x = ''
    x = x+S[0]
    #mylist = list()
    #mylist.append(S[0])
    #print(S)
    #print(mylist)
    for l in range(1,len(S)):
        if S[l] >= x[0] :
            x = S[l]+x
        else :
            x = x + S[l]

    out = "case #" + str(i+1) + ": " + x + "\n"
    fout.write(out) 

fout.close()
fin.close()
