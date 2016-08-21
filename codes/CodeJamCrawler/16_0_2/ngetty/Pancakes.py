import numpy as np

out = open("pancakes-large.out", 'w')
file = "B-large.in"
with open(file, 'r') as infile:
    cases = infile.readlines()[1:]
    count = 0
    for cakes in cases:
        count +=1
        cakes = list(cakes)
        flips = 0
        while "-" in cakes:
            start = cakes[0]
            max = 0
            for cake in cakes:
                if cake == start:
                    max +=1
                else:
                    break
            if start == '-':
                flip_char = '+'
            else:
                flip_char = '-'
            cakes[:max] = [flip_char] * max
            flips+=1
        print >> out, "Case #" + str(count) + ": " + str(flips)
