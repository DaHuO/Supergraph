

def solve(n0):
    #        x      x       x      x        x        x       x       x       x
    ref = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    dico = {}

    tmp = n0.count("X")
    if(tmp != 0):
        dico["SIX"] = tmp
        n0 = n0.replace("S", "",tmp)
        n0 = n0.replace("I", "",tmp)

    tmp = n0.count("S")
    if(tmp != 0):
        dico["SEVEN"] = tmp
        n0 = n0.replace("V", "",tmp)

    tmp = n0.count("V")
    if(tmp != 0):
        dico["FIVE"] = tmp
        n0 = n0.replace("I", "",tmp)

    tmp = n0.count("Z")
    if(tmp != 0):
        dico["ZERO"] = tmp
        n0 = n0.replace("R", "",tmp)
        n0 = n0.replace("O", "",tmp)

    tmp = n0.count("W")
    if(tmp != 0):
        dico["TWO"] = tmp
        n0 = n0.replace("O", "",tmp)
        n0 = n0.replace("T", "",tmp)

    tmp = n0.count("G")
    if(tmp != 0):
        dico["EIGHT"] = tmp
        n0 = n0.replace("T", "",tmp)
        n0 = n0.replace("I", "",tmp)

    tmp = n0.count("T")
    if(tmp != 0):
        dico["THREE"] = tmp
        n0 = n0.replace("R", "",tmp)

    tmp = n0.count("R")
    if(tmp != 0):
        n0 = n0.replace("O", "",tmp)
        dico["FOUR"] = tmp

    tmp = n0.count("O")
    if(tmp != 0):
        n0 = n0.replace("O", "",tmp)
        dico["ONE"] = tmp

    tmp = n0.count("I")
    if(tmp != 0):
        dico["NINE"] = tmp

    n = []

    equi = {}
    for i in range(0, 10):
        equi[ref[i]] = i
    for x in dico.keys():
        n+=str(equi[x])*dico[x]
    return str(sorted(n)).strip("[]").replace(", ","").replace("'","")

t = int(raw_input())

for i in range(1, t+1):
    n = raw_input()
    print "Case #" + str(i) +": "+ solve(n)
