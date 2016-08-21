import sys
from itertools import permutations

vals = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def process(mix):
    mix = mix.replace('\n', '')
    res = ''
    if "Z" in mix:
        cnt = mix.count("Z")
        for c in "ZERO":
            mix = mix.replace(c, '', cnt)
        res = res + '0' * cnt
    if "W" in mix:
        cnt = mix.count("W")
        for c in "TWO":
            mix = mix.replace(c, '', cnt)
        res = res + '2' * cnt
    if "X" in mix:
        cnt = mix.count("X")
        for c in "SIX":
            mix = mix.replace(c, '', cnt)
        res = res + '6' * cnt
    if "G" in mix:
        cnt = mix.count("G")
        for c in "EIGHT":
            mix = mix.replace(c, '', cnt)
        res = res + '8' * cnt
    if "H" in mix:
        cnt = mix.count("H")
        for c in "THREE":
            mix = mix.replace(c, '', cnt)
        res = res + '3' * cnt
    if "U" in mix:
        cnt = mix.count("U")
        for c in "FOUR":
            mix = mix.replace(c, '', cnt)
        res = res + '4' * cnt
    
    if "F" in mix:
        cnt = mix.count("F")
        for c in "FIVE":
            mix = mix.replace(c, '', cnt)
        res = res + '5' * cnt
    
    if "V" in mix:
        cnt = mix.count("V")
        for c in "SEVEN":
            mix = mix.replace(c, '', cnt)
        res = res + '7' * cnt
    
    if "O" in mix:
        cnt = mix.count("O")
        for c in "ONE":
            mix = mix.replace(c, '', cnt)
        res = res + '1' * cnt
    
    if "I" in mix:
        cnt = mix.count("I")
        for c in "NINE":
            mix = mix.replace(c, '', cnt)
        res = res + '9' * cnt
        
        print mix
        
    return ''.join(sorted(res))

if __name__ == '__main__':
    res = ''
    i = 0
    with open('A-large.in', 'r') as file:
        first = True
        for line in file:
            if first:
                first = False
                continue;
            i = i + 1
            res = res + ("Case #%s: %s\n" % (i, process(line)))

    with open('output', 'w+') as file:
        print res
        file.write(res)