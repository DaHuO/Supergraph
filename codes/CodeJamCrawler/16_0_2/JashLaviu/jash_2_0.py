"""
problema 2
panqueques felices
"""

def panquequear(panqueques, cantidad):
    if panqueques[0] == '+':
        panqueques = panqueques[:cantidad].replace('+', '-') + panqueques[cantidad:]
    elif panqueques[0] == '-':
        panqueques = panqueques[:cantidad].replace('-', '+') + panqueques[cantidad:]

    return panqueques


def panquequeFeliz(panqueques):
    for c in panqueques:
        if c == '-':
            return False
    return True


def dameRes(panqueques):
    #recibo una string de la forma '++----++-'
    cantidad = 0

    while not panquequeFeliz(panqueques):
        flag = False
        for i in range(0, len(panqueques)):
            if panqueques[0] != panqueques[i]:
                panqueques = panquequear(panqueques, i)
                cantidad += 1
                flag = True

        if not flag:
            panqueques = "+"
            cantidad += 1


    return cantidad

#tn = 0
#with open ('test.txt','rb') as f:
#    for line in f:
#        tn+=1


t = int(raw_input())
for ti in range(1, t+1):
    casoActual = [s for s in raw_input().split(" ")]
#    casoActual[0] = str(casoActual[0])
    print "Case #{}: {}".format(ti, dameRes(casoActual[0]))
