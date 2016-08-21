freqOfEachLetter = {}

def constructNumbers(S):
    number = [] # store the character of each number
    for s in S:
        if freqOfEachLetter.has_key(s):
            freqOfEachLetter[s] += 1
        else:
            freqOfEachLetter[s] = 1
    # try to make ZERO
    if freqOfEachLetter.has_key('Z'):
        for i in xrange(freqOfEachLetter['Z']):
            number.append('0')
        freqOfEachLetter['E'] -= freqOfEachLetter['Z']
        freqOfEachLetter['R'] -= freqOfEachLetter['Z']
        freqOfEachLetter['O'] -= freqOfEachLetter['Z']
        freqOfEachLetter['Z'] -= freqOfEachLetter['Z']
    # try to make a SIX
    if freqOfEachLetter.has_key('S') and freqOfEachLetter.has_key('I') and freqOfEachLetter.has_key('X'):
        num = min(freqOfEachLetter['S'],freqOfEachLetter['I'],freqOfEachLetter['X'])
        for i in xrange(num):
            number.append('6')
        freqOfEachLetter['S'] -= num
        freqOfEachLetter['I'] -= num
        freqOfEachLetter['X'] -= num
    # try to make a SEVEN
    if freqOfEachLetter.has_key('S') and freqOfEachLetter.has_key('E') and freqOfEachLetter.has_key('V') and freqOfEachLetter.has_key('N') and (freqOfEachLetter['E'] >= 2):
        num = min(freqOfEachLetter['S'],freqOfEachLetter['N'],freqOfEachLetter['E']/2,freqOfEachLetter['V'])
        for i in xrange(num):
            number.append('7')
        freqOfEachLetter['S'] -= num
        freqOfEachLetter['E'] -= num
        freqOfEachLetter['V'] -= num
        freqOfEachLetter['N'] -= num
    # try to make a EIGHT
    if freqOfEachLetter.has_key('E') and freqOfEachLetter.has_key('I') and freqOfEachLetter.has_key('G') and freqOfEachLetter.has_key('H') and freqOfEachLetter.has_key('T'):
        num = min(freqOfEachLetter['E'],freqOfEachLetter['I'],freqOfEachLetter['G'],freqOfEachLetter['H'],freqOfEachLetter['T'])
        for i in xrange(num):
            number.append('8')
        freqOfEachLetter['E'] -= num
        freqOfEachLetter['I'] -= num
        freqOfEachLetter['G'] -= num
        freqOfEachLetter['H'] -= num
        freqOfEachLetter['T'] -= num
    # try to make a TWO
    if freqOfEachLetter.has_key('T') and freqOfEachLetter.has_key('W') and freqOfEachLetter.has_key('O'):
        num = min(freqOfEachLetter['T'],freqOfEachLetter['W'],freqOfEachLetter['O'])
        for i in xrange(num):
            number.append('2')
        freqOfEachLetter['T'] -= num
        freqOfEachLetter['W'] -= num
        freqOfEachLetter['O'] -= num 
    # try to make a FIVE
    if freqOfEachLetter.has_key('F') and freqOfEachLetter.has_key('I') and freqOfEachLetter.has_key('V') and freqOfEachLetter.has_key('E'):
        num = min(freqOfEachLetter['F'],freqOfEachLetter['I'],freqOfEachLetter['V'],freqOfEachLetter['E'])
        for i in xrange(num):
            number.append('5')
        freqOfEachLetter['F'] -= num
        freqOfEachLetter['I'] -= num
        freqOfEachLetter['V'] -= num
        freqOfEachLetter['E'] -= num
    # try to make a FOUR
    if freqOfEachLetter.has_key('F') and freqOfEachLetter.has_key('O') and freqOfEachLetter.has_key('U') and freqOfEachLetter.has_key('R'):
        num = min(freqOfEachLetter['F'],freqOfEachLetter['O'],freqOfEachLetter['U'], freqOfEachLetter['R'])
        for i in xrange(num):
            number.append('4')
        freqOfEachLetter['F'] -= num
        freqOfEachLetter['O'] -= num
        freqOfEachLetter['U'] -= num
        freqOfEachLetter['R'] -= num
    # try to make a THREE
    if freqOfEachLetter.has_key('T') and freqOfEachLetter.has_key('H') and freqOfEachLetter.has_key('R') and freqOfEachLetter.has_key('E') and (freqOfEachLetter['E'] >= 2):
        num = min(freqOfEachLetter['T'],freqOfEachLetter['H'],freqOfEachLetter['R'],freqOfEachLetter['E']/2)
        for i in xrange(num):
            number.append('3')
        freqOfEachLetter['T'] -= num
        freqOfEachLetter['H'] -= num
        freqOfEachLetter['R'] -= num 
        freqOfEachLetter['E'] -= num
    # try to make a NINE
    if freqOfEachLetter.has_key('N') and freqOfEachLetter.has_key('I') and freqOfEachLetter.has_key('E') and freqOfEachLetter['N'] >= 2:
        num = min(freqOfEachLetter['I'],freqOfEachLetter['N'],freqOfEachLetter['E'])
        for i in xrange(num):
            number.append('9')
        freqOfEachLetter['N'] -= num
        freqOfEachLetter['I'] -= num
        freqOfEachLetter['E'] -= num
    # try to make a ONE
    if freqOfEachLetter.has_key('O') and freqOfEachLetter.has_key('N') and freqOfEachLetter.has_key('E'):
        num = min(freqOfEachLetter['O'],freqOfEachLetter['N'],freqOfEachLetter['E'])
        for i in xrange(num):
            number.append('1')
        freqOfEachLetter['O'] -= num
        freqOfEachLetter['N'] -= num
        freqOfEachLetter['E'] -= num
    number.sort()
    return ''.join(number)

if __name__ == "__main__":
    T = int(raw_input())
    for i in xrange(1,T+1):
        s = raw_input()
        n=constructNumbers(s)
        print 'Case #' + str(i) + ': ' + n
        freqOfEachLetter.clear()
