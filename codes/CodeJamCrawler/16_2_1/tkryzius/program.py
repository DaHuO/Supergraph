fin = open('A-large.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())


for i in xrange(t):
    letters = dict()
    s = fin.readline()
    for c in s:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    digits = [0]*10
    if 'Z' in letters and letters['Z'] > 0:
        digits[0] += letters['Z']
        letters['O'] -= digits[0]
    if 'W' in letters and letters['W'] > 0:
        digits[2] += letters['W']
        letters['O'] -= digits[2]
    if 'U' in letters and letters['U'] > 0:
        digits[4] += letters['U']
        letters['F'] -= digits[4]
        letters['O'] -= digits[4]
    if 'G' in letters and letters['G'] > 0:
        digits[8] += letters['G']
        letters['I'] -= digits[8]
        letters['H'] -= digits[8]
    if 'X' in letters and letters['X'] > 0:
        digits[6] += letters['X']
        letters['S'] -= digits[6]
        letters['I'] -= digits[6]
    if 'H' in letters and letters['H'] > 0:
        digits[3] += letters['H']
    if 'O' in letters and letters['O'] > 0:
        digits[1] += letters['O']
    if 'F' in letters and letters['F'] > 0:
        digits[5] += letters['F']
        letters['I'] -= digits[5]
    if 'S' in letters and letters['S'] > 0:
        digits[7] += letters['S']
    if 'I' in letters and letters['I'] > 0:
        digits[9] += letters['I']

    number = ''
    for n in xrange(10):
        number += str(n)*digits[n]       
    fout.write('Case #' + str(i + 1) + ': ' + ' ' + number + '\n')

fout.close()

print 'FINISHED'
