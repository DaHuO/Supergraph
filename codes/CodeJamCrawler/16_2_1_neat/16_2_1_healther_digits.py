import sys
#import argpase

from collections import Counter
import numpy as np 


numbers = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
}

backtrans = [
    ('Z', 0),
    ('W', 2),
    ('U', 4),
    ('X', 6),
    ('G', 8),
    ('H', 3),
    ('F', 5),
    ('V', 7),
    ('I', 9),
    ('O', 1),
]



def number_from_string(inputline):
    line = inputline

    counter = dict(Counter(line).most_common())
    digits = []

    for bt in backtrans: 
        try:
            char = bt[0]
            number = bt[1]
            letters = numbers[number]
            frequency = counter[char]

            digits.extend(frequency*[number])
            for s in letters:
                counter[s] -= frequency
        except KeyError:
            pass

    digits.sort()
    ret = "".join([str(i) for i in digits])

    return ret



if "__main__" == __name__:
    
    # print(sys.argv[1])
    inputfile = sys.argv[1]

    out = []
    with open(inputfile, 'r') as f:
        T = int(f.readline())
        for _ in range(T):
            out.append(number_from_string(f.readline()))
    
    with open("out_"+inputfile, 'w') as f:
        for i, o in enumerate(out):
            f.write("Case #{}: {}\n".format(i+1, o))
            print("Case #{}: {}".format(i+1, o))
