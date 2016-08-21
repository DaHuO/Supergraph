# pancakes


entrada = open('in-large.in','r')
salida = open('out-large.out','w')

casos = int(entrada.readline().rstrip('\n'))

def num_clusters(s):
    res = 1
    for c in xrange(len(s)-1):
        if s[c]!=s[c+1]:
            res = res + 1
    return res

for caso in xrange(casos):
    tarta = entrada.readline().rstrip('\n')
    clusters = num_clusters(tarta)
    if tarta[-1] == '+':
        clusters = clusters - 1

    salida.write("Case #%d: %d\n" % (caso + 1, clusters))





