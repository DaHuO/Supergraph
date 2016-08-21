import sys
import math
import numpy # http://www.numpy.org/
import string
import tkinter as tk
from tkinter.filedialog import askopenfilename
import itertools

root = tk.Tk()
root.withdraw()

filename = askopenfilename()
fInput = open(filename, 'r')
fOutput = open(filename.replace(".in", ".txt"), 'w+')

T = int(fInput.readline())

for t in range(T):
    order = fInput.readline().rstrip()
    word =[]
    for i in range(len(order)):
        if order[i] < max(order):
            if len(word) > 0:
                if order[i] >= word[0]:
                    word.insert(0, order[i])
                else:
                    word.append(order[i])
            else:
                word.append(order[i])
        if order[i] == max(order):
            word.insert(0, order[i])

    result = ''.join(word)
        
    fOutput.write("Case #{}: {}\n".format(t+1, result))
    print("Case #{}: {}".format(t+1, result))
    
fInput.close()
fOutput.close()
