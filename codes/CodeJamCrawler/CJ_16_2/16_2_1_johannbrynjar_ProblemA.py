def countNumberOfAlpha(string, s):
	return string.count(s)

def removeAlpha(string, word, maxreplace):
    s = string
    for w in word:
        s = s.replace(w, '', maxreplace)
    return s

if __name__ == "__main__":
    try:
        dict = [['ZERO', 'Z', 0], ['TWO', 'W', 2], ['FOUR', 'U', 4], ['SIX', 'X', 6], ['EIGHT', 'G', 8], ['THREE', 'H', 3], ['FIVE', 'F', 5], ['SEVEN', 'S', 7], ['ONE', 'O', 1], ['NINE', 'I', 9]]
       	numberOfCase = int(raw_input(''))
        for i in xrange(numberOfCase):
            number = [0,0,0,0,0,0,0,0,0,0]
            S = raw_input('')
            output = '';
            for d in dict:
                numberOfAlpha = countNumberOfAlpha(S, d[1])
                number[d[2]] = numberOfAlpha
                S = removeAlpha(S, d[0], numberOfAlpha)
            for y, times in enumerate(number):
                for t in xrange(0,times):
                    output = output + str(y)
            print 'Case #{0}: {1}'.format(i+1, output)
    except (EOFError):
        print ''

