t = int(raw_input())

def find_number(exclusive, spelt, letters):
    count = 0
    while exclusive in letters and letters[exclusive] > 0:
        for l in spelt:
            letters[l] -= 1
        count += 1
    return count

for x in xrange(1,t+1):
    result = {}
    letters = {}
    s = raw_input()
    for l in s:
        if l not in letters:
            letters[l] = 0
        letters[l] += 1
    result[0] = find_number('Z', 'ZERO', letters)
    result[2] = find_number('W', 'TWO', letters)
    result[4] = find_number('U', 'FOUR', letters)
    result[5] = find_number('F', 'FIVE', letters)
    result[6] = find_number('X', 'SIX', letters)
    result[7] = find_number('V', 'SEVEN', letters)
    result[8] = find_number('G', 'EIGHT', letters)
    result[9] = find_number('I', 'NINE', letters)
    result[1] = find_number('N', 'ONE', letters)
    result[3] = find_number('H', 'THREE', letters)
    number = ''
    for n in sorted(result.keys()):
        number += str(n) * result[n]
    print "Case #%d: %s" % (x, number)
