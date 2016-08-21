f = open('input.in', 'r')
output = open('output.out', 'w')
lignes=iter(f.read().splitlines())
nbTests=int(next(lignes))

def renverser(unPaquet):
    retour = []
    for index in range(0,len(unPaquet)):
        if unPaquet[len(unPaquet) - 1 - index] == "-":
            retour.append("+")
        else:
            retour.append("-")
    return retour

def renverserFull(laLigne,index):
    nouveauxPremiers = renverser(laLigne[0:index+1])
    laLigne = nouveauxPremiers + laLigne[index+1:len(laLigne)]
    return laLigne

for numeroTest in range(0,nbTests):

    laLigne = list(next(lignes))
    compteur = 0
    while("-" in laLigne):
        if laLigne[0] == "-":
            dernierIndexDeMoins = 0
            for index,element in enumerate(laLigne):
                if element == "-":
                    dernierIndexDeMoins = index
            laLigne = renverserFull(laLigne,dernierIndexDeMoins)
        #Autrement on gère le premier morceau
        else:
            premierPaquetPlus = 0
            for index,element in enumerate(laLigne):
                if element == "-":
                    break
                else:
                    premierPaquetPlus = index
            laLigne = renverserFull(laLigne,premierPaquetPlus)
        compteur += 1
    reponse="" + str(compteur)
    output.write("Case #"+str(numeroTest+1)+": "+reponse)
    if numeroTest<nbTests-1:
        output.write("\n")
    print("Reponse="+reponse)