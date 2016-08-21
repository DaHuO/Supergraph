#
# problemA.py
#

# Import
import sys
sys.dont_write_bytecode = True
sys.path.append('../')
from gcj import Problem
from gcj.utils import Timer

# Parser
def parser(fin):
    return fin.readWord()

# Solver
# E 9
# G 1
# F 2
# I 4
# H 2
# O 4
# N 4
# S 2
# R 3
# U 1
# T 3
# W 1
# V 2
# X 1
# Z 1
E, G, F, I, H, O, N, S, R, U, T, W, V, X, Z = 'E', 'G', 'F', 'I', 'H', 'O', 'N', 'S', 'R', 'U', 'T', 'W', 'V', 'X', 'Z'
NUMBERS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
def solver(data):
    letters = list(data)
    number = []
    
    while letters:
    
        # ZERO
        if Z in letters:
            number.append(0)
            letters.remove(Z)
            letters.remove(E)
            letters.remove(R)
            letters.remove(O)
            continue
            
        # TWO
        if W in letters:
            number.append(2)
            letters.remove(T)
            letters.remove(W)
            letters.remove(O)
            continue
        
        # FOUR
        if U in letters:
            number.append(4)
            letters.remove(F)
            letters.remove(O)
            letters.remove(U)
            letters.remove(R)
            continue
        
        # SIX
        if X in letters:
            number.append(6)
            letters.remove(S)
            letters.remove(I)
            letters.remove(X)
            continue
        
        # EIGHT
        if G in letters:
            number.append(8)
            letters.remove(E)
            letters.remove(I)
            letters.remove(G)
            letters.remove(H)
            letters.remove(T)
            continue
            
        
        # FIVE
        if F in letters:
            number.append(5)
            letters.remove(F)
            letters.remove(I)
            letters.remove(V)
            letters.remove(E)
            continue
            
        # ONE
        if O in letters:
            number.append(1)
            letters.remove(O)
            letters.remove(N)
            letters.remove(E)
            continue
            
        # THREE
        if H in letters:
            number.append(3)
            letters.remove(T)
            letters.remove(H)
            letters.remove(R)
            letters.remove(E)
            letters.remove(E)
            continue
            
        # SEVEN
        if V in letters:
            number.append(7)
            letters.remove(S)
            letters.remove(E)
            letters.remove(V)
            letters.remove(E)
            letters.remove(N)
            continue
            
        # NINE
        if I in letters:
            number.append(9)
            letters.remove(N)
            letters.remove(I)
            letters.remove(N)
            letters.remove(E)
            continue
        
    # letters = []
    # for number in NUMBERS:
        # letters.extend(list(number))
    # print letters
    # lettersfreq = {}
    # for letter in letters:
        # if not letter in lettersfreq:
            # lettersfreq[letter] = 0
        # lettersfreq[letter] += 1
    # for key in lettersfreq:
        # print key, lettersfreq[key]
    number.sort()
    return ''.join(map(str,number))

# Main
if __name__ == '__main__':
    with Timer('Problem A'):
        Problem(parser, solver).run()
