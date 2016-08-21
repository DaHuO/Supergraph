def digits(string):
    s = list(string)
    words = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    d = 0
    numbers = []
    # remove ZERO
    while s.count('Z') > 0:
        numbers.append('0')
        for c in words[0]:
            s.remove(c)
    # remove TWO
    while s.count('W') > 0:
        numbers.append('2')
        for c in words[2]:
            s.remove(c)
    # remove SIX
    while s.count('X') > 0:
        numbers.append('6')
        for c in words[6]:
            s.remove(c)
    # remove EIGHT
    while s.count('G') > 0:
        numbers.append('8')
        for c in words[8]:
            s.remove(c)
    # remove THREE
    while s.count('H') > 0:
        numbers.append('3')
        for c in words[3]:
            s.remove(c)     
    # remove FOUR
    while s.count('U') > 0:
        numbers.append('4')
        for c in words[4]:
            s.remove(c)
    # remove FIVE
    while s.count('F') > 0:
        numbers.append('5')
        for c in words[5]:
            s.remove(c)
    # remove SEVEN
    while s.count('V') > 0:
        numbers.append('7')
        for c in words[7]:
            s.remove(c)
    # remove ONE
    while s.count('O') > 0:
        numbers.append('1')
        for c in words[1]:
            s.remove(c)
    # remove NINE
    while s.count('N') > 0:
        numbers.append('9')
        for c in words[9]:
            s.remove(c)
    
    numbers.sort()
    return ''.join(numbers)

if __name__ == '__main__':
    for T in range(int(raw_input().strip())):
        s = raw_input().strip()
        print "Case #%d: %s" % (T+1, digits(s))