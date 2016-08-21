entrada = open('small.in','r')
salida = open('small.out','w')

N = int(entrada.readline().rstrip('\n'))
for caso in xrange(N):
    KCS = map(int,entrada.readline().strip('\n').split(' '))
    K = KCS[0]
    C = KCS[1]
    S = KCS[2]


    tam = K**C # tamano tile final
    inc = tam / K

    res = []

    if C==1:
        mirar = 1
        for i in xrange(K):
            res.append(mirar)
            mirar = mirar + inc
    else:
        mirar = inc+1
        for i in xrange(K-1):
            res.append(mirar)
            mirar = mirar + inc

    if not res and S>0:
        salida.write("Case #%d: %s\n" % ((caso + 1), 1 ))
    elif C==1 and S<>K:
        salida.write("Case #%d: IMPOSSIBLE\n" % (caso + 1))
    elif len(res) <= S:
        salida.write("Case #%d: %s\n" % ((caso + 1)," ".join(map(str,res))))
    else:
        salida.write("Case #%d: IMPOSSIBLE\n" % (caso + 1))


