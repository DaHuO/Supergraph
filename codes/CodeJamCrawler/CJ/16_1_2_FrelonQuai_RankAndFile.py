from itertools import chain

f = open('input.in', 'r')
output = open('output.out', 'w')
lignes=iter(f.read().splitlines())
nbTests=int(next(lignes))


for numeroTest in range(0,nbTests):

    N = int(next(lignes))

    lesLignes = []

    for element in range(0,2*N-1):
        lesLignes.append([int(x) for x in next(lignes).split(" ")])

    print(lesLignes)

    tousLesNombres = list(chain(*lesLignes))

    print(tousLesNombres)

    setTousLesNombres = set(tousLesNombres)
    aTrier = []
    for element in setTousLesNombres:
        nb = len([nombre for nombre in tousLesNombres if nombre == element])
        if nb % 2 == 1:
            aTrier.append(element)

    aTrier = sorted(aTrier)

    reponse = "" + " ".join([str(x) for x in aTrier])

    output.write("Case #"+str(numeroTest+1)+": "+reponse)
    if numeroTest<nbTests-1:
        output.write("\n")
    print("Reponse="+reponse)