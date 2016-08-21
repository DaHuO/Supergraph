from itertools import groupby
import string

f = open('input.in', 'r')
output = open('output.out', 'w')
lignes=iter(f.read().splitlines())
nbTests=int(next(lignes))


for numeroTest in range(0,nbTests):
    N = int(next(lignes))
    senateurs = [int(x) for x in next(lignes).split(" ")]

    print(N)
    print(senateurs)
    lettres = string.ascii_uppercase
    restant = []

    for position,nbSenateurs in enumerate(senateurs):
        restant += lettres[position] * nbSenateurs

    print(restant)
    reponse = []
    
    def situationInstable(restant):
        for key,group in groupby(restant):
            if 2 * len(list(group)) > len(restant):
                return True
        return False

    def obtenirLettreAPopper(restant):
        lettresDistinctes = set(restant)
        lettreAPopper = ""
        nbApparitions = 0
        for lettre in lettresDistinctes:
            leMax = len([x for x in restant if x == lettre])
            if(leMax > nbApparitions):
                nbApparitions = leMax
                lettreAPopper = lettre
        return lettreAPopper

    while len(restant) > 0:
        lettreAPopper = obtenirLettreAPopper(restant)
        restant.remove(lettreAPopper)
        
        if situationInstable(restant):
            autreLettre = obtenirLettreAPopper(restant)
            restant.remove(autreLettre)
            lettreAPopper += autreLettre

        reponse.append(lettreAPopper)


    print(reponse)

    reponse = " ".join(reponse)
    output.write("Case #"+str(numeroTest+1)+": "+reponse)
    if numeroTest<nbTests-1:
        output.write("\n")
    print("Reponse="+reponse)