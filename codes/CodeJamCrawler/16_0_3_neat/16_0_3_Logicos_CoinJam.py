def ontbindt(bits,denom):
    denom2 = 1
    getal = 0
    while bits:
        getal += (int(bits[-1]) * denom2)
        bits = bits[:-1]
        denom2 *= denom
    return getal

def volOntbindt(bits):
    boolie = True
    delers = []
    for getal in range(2,11):
        deler = vindtDeler(ontbindt(bits,getal))
        #Kan beter
        if not deler:
            boolie = False
            break
        delers.append(deler)
    if boolie:
        print("{} {} {} {} {} {} {} {} {} {}".format(bits,delers[0],delers[1],delers[2],delers[3],delers[4],delers[5],delers[6],delers[7],delers[8]))
    return boolie

def vindtDeler(getal):
    i = 2
    while i ** 2 <= getal:
        if not getal%i:
            return i
        i += 1
    return 0

print("Case #1:")
a = 1
for i in range(2**14,2**15-1):
    if volOntbindt(str(bin(i)[2:] + "1")):
        a += 1
    if a > 50:
        break
