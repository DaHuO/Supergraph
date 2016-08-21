import sys

def removeChar(S, c):
    for i in range(len(S)):
            if S[i] == c:
                del S[i]
                break

def repPrint(c, n):
    for i in range(n):
        print(str(c), end='')
    
def solve(S):
    if "Z" in S:        
        removeChar(S, 'Z')
        removeChar(S, "E")
        removeChar(S, "R")
        removeChar(S, "O")
        print('0', end='')
        solve(S)

    twos=0
    while("W" in S):
        removeChar(S, "T")
        removeChar(S, "W")
        removeChar(S, "O")
        twos+=1

    fours=0
    while("U" in S):
        removeChar(S, "F")
        removeChar(S, "O")
        removeChar(S, "U")
        removeChar(S, "R")
        fours+=1

    ones = 0
    while("O" in S):
        removeChar(S, "O")
        removeChar(S, "N")
        removeChar(S, "E")
        ones+=1
    repPrint(1, ones)
    repPrint(2, twos)

    sixes = 0
    while("X" in S):
        removeChar(S, "S")
        removeChar(S, "I")
        removeChar(S, "X")
        sixes+=1

    eights = 0
    while("G" in S):
        removeChar(S, "E")
        removeChar(S, "I")
        removeChar(S, "G")
        removeChar(S, "H")
        removeChar(S, "T")
        eights+=1

    threes = 0
    while("T" in S):
        removeChar(S, "T")
        removeChar(S, "H")
        removeChar(S, "R")
        removeChar(S, "E")
        removeChar(S, "E")
        threes+=1

    fives = 0
    while("F" in S):
        removeChar(S, "F")
        removeChar(S, "I")
        removeChar(S, "V")
        removeChar(S, "E")
        fives+=1

    sevens = 0
    while("V" in S):
        removeChar(S, "S")
        removeChar(S, "E")
        removeChar(S, "V")
        removeChar(S, "E")
        removeChar(S, "N")
        sevens+=1

    nines = 0
    while("N" in S):
        removeChar(S, "N")
        removeChar(S, "I")
        removeChar(S, "N")
        removeChar(S, "E")
        nines+=1

    repPrint(3, threes)
    repPrint(4, fours)
    repPrint(5, fives)
    repPrint(6, sixes)
    repPrint(7, sevens)
    repPrint(8, eights)
    repPrint(9, nines)
    

def main():
    T = int(sys.stdin.readline())
    for i in range(1, T+1):
        S = list(sys.stdin.readline())[:-1]
        print('Case #'+str(i)+': ', end='')
        solve(S)
        print()
main()
