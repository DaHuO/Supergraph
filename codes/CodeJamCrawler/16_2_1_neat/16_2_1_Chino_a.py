import sys


#"ZERO",  z
#"TWO",   w 
#"SIX",   x
#"SEVEN", s 
#"EIGHT", g
#"THREE", h
#"FOUR",  r
#"ONE",   o
#"FIVE",  f
#"NINE"   n


def find(s) :
    letters = dict()
    digits = dict()
    a = "ZWXSGHROFI"
    for d in range(0,9) :
        digits[d] = 0

    for c in a :
        letters[c] = 0
    #print letters
    for c in s :
        #print c
        if c not in letters :
            letters[c] = 0
        letters[c] += 1

        #print letters

    #"ZERO",  z
    if letters['Z'] > 0:
        r = letters['Z']
        digits[0] = r
        letters['Z'] -= r
        letters['E'] -= r
        letters['R'] -= r
        letters['O'] -= r
    #"TWO",   w 
    if letters['W'] > 0:
        r = letters['W']
        digits[2] = r
        letters['T'] -= r
        letters['W'] -= r
        letters['O'] -= r
    #"SIX",   x
    if letters['X'] > 0:
        r = letters['X']
        digits[6] = r
        letters['S'] -= r
        letters['I'] -= r
        letters['X'] -= r
    #"SEVEN", s 
    if letters['S'] > 0:
        r = letters['S']
        digits[7] = r
        letters['S'] -= r
        letters['E'] -= 2*r
        letters['V'] -= r
        letters['N'] -= r
    #"EIGHT", g
    if letters['G'] > 0:
        r = letters['G']
        digits[8] = r
        letters['E'] -= r
        letters['I'] -= r
        letters['G'] -= r
        letters['H'] -= r
        letters['T'] -= r
    #"THREE", h
    if letters['H'] > 0:
        r = letters['H']
        digits[3] = r
        letters['T'] -= r
        letters['H'] -= r
        letters['R'] -= r
        letters['E'] -= 2*r
    #"FOUR",  r
    if letters['R'] > 0:
        r = letters['R']
        digits[4] = r
        letters['F'] -= r
        letters['O'] -= r
        letters['U'] -= r
        letters['R'] -= r
    #"ONE",   o
    if letters['O'] > 0:
        r = letters['O']
        digits[1] = r
        letters['E'] -= r
        letters['N'] -= r
        letters['O'] -= r
    #"FIVE",  f
    if letters['F'] > 0:
        r = letters['F']
        digits[5] = r
        letters['F'] -= r
        letters['I'] -= r
        letters['V'] -= r
        letters['E'] -= r
    #"NINE"   n
    if letters['I'] > 0:
        r = letters['I']
        digits[9] = r
    #print digits
    #print letters
    ret = ""
    for d in digits :
        c = str(d)
        for i in range(digits[d]) :
            ret += c
    return ret



if __name__ == '__main__':
    T = int(sys.stdin.readline())
    #print(T)
    for i in range(T) :
        s = sys.stdin.readline()
        s = s.replace("\n", "")
        res = find(s)
        print "Case #%d: %s" % (i+1, res)
