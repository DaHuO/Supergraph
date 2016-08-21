Name = "A-large.in"
fin = open(Name, 'r')
out = open("A2.out", 'a')
T = int(fin.readline())
A = '0123456789'
B = list(A)

for i in range(T):
    print(i)
    D = fin.readline()
    intD = int(D)
    emptyS = ''
    Ans = []
    if intD == 0:
        P = "INSOMNIA"
    else :
        for k in range(100):
            D = intD*(k+1)
            emptyS = emptyS + str(D)
            liD = list(emptyS)
            liD.sort()
            #print(liD)
            for s in liD:
                if liD.count(s)>1:
                    for j in range(1, liD.count(s)):
                        liD.remove(s)
                        sjoin = ''.join(liD)
                        if sjoin == A:
                            Ans.append(D)
                                               
        P = Ans[0]
    out.write("Case #"+ str(int(i)+1) +": "+ str(P)+"\n")
fin.seek(0,0)
out.seek(0,0)
fin.close()
out.close()
    
