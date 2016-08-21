def number(s):
    f = {}
    if not len(s):
        return []
    
    n = []
    while "Z" in s:
        n.append('0')
        for k in "ZERO":
            s = s.replace(k, '', 1)
    while "G" in s:
        n.append('8')
        for k in "EIGHT":
            s = s.replace(k, '', 1)
    while "X" in s:
        n.append('6')
        for k in "SIX":
            s = s.replace(k, '', 1)
    while "U" in s:
        n.append('4')
        for k in "FOUR":
            s = s.replace(k, '', 1)
    while "W" in s:
        n.append('2')
        for k in "TWO":
            s = s.replace(k, '', 1)
    while "O" in s:
        n.append('1')
        for k in "ONE":
            s = s.replace(k, '', 1)
    while "H" in s:
        n.append('3')
        for k in "THREE":
            s = s.replace(k, '', 1)
    while "F" in s:
        n.append('5')
        for k in "FIVE":
            s = s.replace(k, '', 1)    
    while "V" in s:
        n.append('7')
        for k in "SEVEN":
            s = s.replace(k, '', 1)        
    while "N" in s:
        n.append('9')
        for k in "NINE":
            s = s.replace(k, '', 1)
    return "".join(sorted(n))


t = int(raw_input())

for i in range(t):
    string = raw_input()
    print "Case #%d: %s" % (i+1, number(string))
