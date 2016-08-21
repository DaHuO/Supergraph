from sys import *
from math import *

def solve(case, nbParti, tabNbParti) :
    solus = ""
    while max(tabNbParti) != 0 :
        maximum = max(tabNbParti)
        indexElement = tabNbParti.index(maximum)
        tabNbParti[indexElement] -= 1
        if indexElement == 0 :
            solus = solus + "A"
        elif indexElement == 1 :
            solus = solus + "B"
        elif indexElement == 2 :
            solus = solus + "C"
        elif indexElement == 3 :
            solus = solus + "D"
        elif indexElement == 4 :
            solus = solus + "E"
        elif indexElement == 5 :
            solus = solus + "F"
        elif indexElement == 6 :
            solus = solus + "G"
        elif indexElement == 7 :
            solus = solus + "H"
        elif indexElement == 8 :
            solus = solus + "I"
        elif indexElement == 9 :
            solus = solus + "J"
        elif indexElement == 10 :
            solus = solus + "K"
        elif indexElement == 11 :
            solus = solus + "L"
        elif indexElement == 12 :
            solus = solus + "M"
        elif indexElement == 13 :
            solus = solus + "N"
        elif indexElement == 14 :
            solus = solus + "O"
        elif indexElement == 15 :
            solus = solus + "P"
        elif indexElement == 16 :
            solus = solus + "Q"
        elif indexElement == 17 :
            solus = solus + "R"
        elif indexElement == 18 :
            solus = solus + "S"
        elif indexElement == 19 :
            solus = solus + "T"
        elif indexElement == 20 :
            solus = solus + "U"
        elif indexElement == 21 :
            solus = solus + "V"
        elif indexElement == 22 :
            solus = solus + "W"
        elif indexElement == 23 :
            solus = solus + "X"
        elif indexElement == 24 :
            solus = solus + "Y"
        elif indexElement == 25 :
            solus = solus + "Z"
        nbTotal = sum(tabNbParti)
        nouveauMaximum = max(tabNbParti)
        indexElement = tabNbParti.index(nouveauMaximum)
        tabNbParti[indexElement] -= 1
        nbTotal = sum(tabNbParti)
        if nbTotal == 0 or tabNbParti.index(max(tabNbParti)) / nbTotal <= 0.5 :
            if indexElement == 0 :
                solus = solus + "A"
            elif indexElement == 1 :
                solus = solus + "B"
            elif indexElement == 2 :
                solus = solus + "C"
            elif indexElement == 3 :
                solus = solus + "D"
            elif indexElement == 4 :
                solus = solus + "E"
            elif indexElement == 5 :
                solus = solus + "F"
            elif indexElement == 6 :
                solus = solus + "G"
            elif indexElement == 7 :
                solus = solus + "H"
            elif indexElement == 8 :
                solus = solus + "I"
            elif indexElement == 9 :
                solus = solus + "J"
            elif indexElement == 10 :
                solus = solus + "K"
            elif indexElement == 11 :
                solus = solus + "L"
            elif indexElement == 12 :
                solus = solus + "M"
            elif indexElement == 13 :
                solus = solus + "N"
            elif indexElement == 14 :
                solus = solus + "O"
            elif indexElement == 15 :
                solus = solus + "P"
            elif indexElement == 16 :
                solus = solus + "Q"
            elif indexElement == 17 :
                solus = solus + "R"
            elif indexElement == 18 :
                solus = solus + "S"
            elif indexElement == 19 :
                solus = solus + "T"
            elif indexElement == 20 :
                solus = solus + "U"
            elif indexElement == 21 :
                solus = solus + "V"
            elif indexElement == 22 :
                solus = solus + "W"
            elif indexElement == 23 :
                solus = solus + "X"
            elif indexElement == 24 :
                solus = solus + "Y"
            elif indexElement == 25 :
                solus = solus + "Z"
        else :
            tabNbParti[indexElement] += 1
        solus = solus + " "
    
    solution = solus.strip()
    print("Case #{0}: {1}".format(case, solution))

cases = int(input())
for i in range(1, cases + 1) :
    nbParti = int(input())
    tabNbParti = input().split()
    for j in range(len(tabNbParti)) :
        tabNbParti[j] = int(tabNbParti[j])
    solve(i, nbParti, tabNbParti)
