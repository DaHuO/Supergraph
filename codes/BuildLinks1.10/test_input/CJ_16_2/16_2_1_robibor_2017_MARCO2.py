#!/usr/bin/python

legend = {0:"ZERO",
          1:'ONE',
          2:'TWO',
          3:'THREE',
          4:'FOUR',
          5:'FIVE',
          6:'SIX',
          7:'SEVEN',
          8:'EIGHT',
          9:'NINE'}

map = [(0, 'Z'),
       (2, 'W'),
       (4, 'U'),
       (6, 'X'),
       (7, 'S'),
       (5, 'V'),
       (8, 'G'),
       (3, 'T'),
       (9, 'I'),
       (1, 'N')
]

def solve(N):
    out=[]
    data = {}
    for el in N:
        if data.get(el, 0):
            data[el] += 1
        else:
            data[el] = 1
    for el in map:
        if data.get(el[1], 0):
            togli=data.get(el[1], 0)
            for letter in legend[el[0]]:
                data[letter] -= togli
            for n in range(togli):
                out.append(int(el[0]))
    out = [str(el) for el in out]
    res = ''.join(sorted(out))
    return res

def read():
    with open("A.in", "r") as filein:
        with open("A.out", "w") as fileout:
            lines = filein.readlines()
            ii=1
            for line in lines[1:]:
                N = line.strip()
                out = solve(N)
                mystr = "Case #" + str(ii) + ": " + out + "\n"
                ii += 1
                fileout.write(mystr)

if __name__ == '__main__':
    read()
