# int(fInput.readline())
# fInput.readline().rstrip()
# [int(s) for s in str.split(fInput.readline().rstrip(),' ')]
# result = ' '.join(str(result[n]) for n in range(N))
import sys
import math
import numpy # http://www.numpy.org/
import string
import tkinter as tk
from tkinter.filedialog import askopenfilename

def debug(*args):
    print(" ".join(str(arg) for arg in args))
    return

root = tk.Tk()
root.withdraw()

filename = askopenfilename()
fInput = open(filename, 'r')
fOutput = open(filename.replace(".in", ".txt"), 'w+')

T = int(fInput.readline())

for t in range(T):
    S = fInput.readline().rstrip()

    unique = 'Z,E,R,O,O,N,E,T,W,O,T,H,R,E,E,F,O,U,R,F,I,V,E,S,I,X,S,E,V,E,N,E,I,G,H,T,N,I,N,E'
    unique = unique.split(',')

    uniques = []

    for i in range(len(unique)):
        if unique[i] not in uniques:
            uniques.append(unique[i])

    uniques.sort()
    
    letCounts = [0]*len(uniques)

    for i in range(len(S)):
        letCounts[uniques.index(S[i])] += 1

    numbers = ['ZERO', "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    order = [0, 2, 6, 8, 3, 4, 5, 9, 1, 7]
    letter = ['Z', 'W', 'X', 'G', 'H', 'R', 'F', 'I', 'O', 'S']

    result = []
    while sum(letCounts) > 0:
        for i in range(len(order)):
            while letCounts[uniques.index(letter[i])] > 0:
                for j in range(len(numbers[order[i]])):
                    letCounts[uniques.index(numbers[order[i]][j])] -= 1
                result.append(order[i])

    result.sort()
    result = ''.join(str(result[n]) for n in range(len(result)))
    print('Case #{}: {}'.format(t+1, result))
    fOutput.write('Case #{}: {}\n'.format(t+1, result))

fInput.close()
fOutput.close()
