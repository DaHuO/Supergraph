import numpy as np
from collections import Counter
from math import *


f = file('input.txt')
out = open('output.txt', 'w+')
T = int(f.readline())
for t in range(1, T + 1):
    sides = str(f.readline())
    sad_faces = 0
    for i in range(len(sides)-2):
        if sides[i] != sides[i+1]:
            sad_faces += 1
    flips = sad_faces
    if (sides[0] == '-' and flips % 2 == 0) or (sides[0] == '+' and flips % 2 == 1):
        flips += 1
    line = "Case #" + str(t) + ": " + str(flips)
    print(line)
    out.write(line + "\n")
f.close()
out.close()
