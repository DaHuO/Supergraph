f = open('A-large.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())


for t in xrange(T):
    number = ''
    letters = [0]*26
    digits = [0]*10
    N = f.readline().strip()
    for letter in N:
        letters[ord(letter) - ord('A')] += 1
    while letters[ord('Z') - ord('A')] > 0:
        letters[ord('Z') - ord('A')] -= 1
        letters[ord('E') - ord('A')] -= 1
        letters[ord('R') - ord('A')] -= 1
        letters[ord('O') - ord('A')] -= 1
        digits[0] += 1
    while (letters[ord('W') - ord('A')] > 0):
        letters[ord('O') - ord('A')] -= 1
        letters[ord('T') - ord('A')] -= 1
        letters[ord('W') - ord('A')] -= 1
        digits[2] += 1
    while (letters[ord('U') - ord('A')] > 0):
        letters[ord('F') - ord('A')] -= 1
        letters[ord('O') - ord('A')] -= 1
        letters[ord('U') - ord('A')] -= 1
        letters[ord('R') - ord('A')] -= 1
        digits[4] += 1
    while (letters[ord('X') - ord('A')] > 0):
        letters[ord('S') - ord('A')] -= 1
        letters[ord('I') - ord('A')] -= 1
        letters[ord('X') - ord('A')] -= 1
        digits[6] += 1
    while (letters[ord('G') - ord('A')] > 0):
        digits[8] += 1
        letters[ord('E') - ord('A')] -= 1
        letters[ord('I') - ord('A')] -= 1
        letters[ord('G') - ord('A')] -= 1
        letters[ord('H') - ord('A')] -= 1
        letters[ord('T') - ord('A')] -= 1
    while (letters[ord('O') - ord('A')] > 0) and (letters[ord('N') - ord('A')] > 0) and (letters[ord('E') - ord('A')] > 0):
        digits[1] += 1
        letters[ord('O') - ord('A')] -= 1
        letters[ord('N') - ord('A')] -= 1
        letters[ord('E') - ord('A')] -= 1
    while (letters[ord('T') - ord('A')] > 0) and (letters[ord('H') - ord('A')] > 0) and (letters[ord('E') - ord('A')] > 1) and (letters[ord('R') - ord('A')] > 0):
        digits[3] += 1
        letters[ord('T') - ord('A')] -= 1
        letters[ord('H') - ord('A')] -= 1
        letters[ord('E') - ord('A')] -= 2
        letters[ord('R') - ord('A')] -= 1

    while (letters[ord('F') - ord('A')] > 0) and (letters[ord('I') - ord('A')] > 0) and (letters[ord('V') - ord('A')] > 0) and (letters[ord('E') - ord('A')] > 0):
        digits[5] += 1
        letters[ord('F') - ord('A')] -= 1
        letters[ord('I') - ord('A')] -= 1
        letters[ord('V') - ord('A')] -= 1
        letters[ord('E') - ord('A')] -= 1

    while (letters[ord('S') - ord('A')] > 0) and (letters[ord('E') - ord('A')] > 1) and (letters[ord('V') - ord('A')] > 0) and (letters[ord('N') - ord('A')] > 0):
        digits[7] += 1
        letters[ord('S') - ord('A')] -= 1
        letters[ord('E') - ord('A')] -= 2
        letters[ord('V') - ord('A')] -= 1
        letters[ord('N') - ord('A')] -= 1
    while (letters[ord('N') - ord('A')] > 1) and (letters[ord('I') - ord('A')] > 0) and (letters[ord('E') - ord('A')] > 0):
        digits[9] += 1
        letters[ord('N') - ord('A')] -= 2
        letters[ord('I') - ord('A')] -= 1
        letters[ord('E') - ord('A')] -= 1
    for i in range(len(digits)):
        while digits[i] > 0:
            digits[i] -= 1
            number += str(i)
    s = "Case #%d: %s\n" % (t+1, number)
    
    o.write(s)