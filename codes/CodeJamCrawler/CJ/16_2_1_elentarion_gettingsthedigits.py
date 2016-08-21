def extract_digits(nlist, llist, digit, discriminant, word):
        nlist += list(int(x) for x in (digit * llist.count(discriminant)))
        llist = eliminate_word(llist, word, llist.count(discriminant))
        return (nlist, llist)

def eliminate_word(llist, word, nb):
        for i in range(0, nb):
                for character in word:
                        llist = llist[:llist.index(character)] + llist[llist.index(character)+1:]

        return llist

t = int(raw_input())
for i in xrange(1, t + 1):
        llist = list(raw_input())
        nlist = []

        nlist, llist = extract_digits(nlist, llist, '0', 'Z', 'ZERO')
        nlist, llist = extract_digits(nlist, llist, '2', 'W', 'TWO')
        nlist, llist = extract_digits(nlist, llist, '6', 'X', 'SIX')
        nlist, llist = extract_digits(nlist, llist, '8', 'G', 'EIGHT')
        nlist, llist = extract_digits(nlist, llist, '3', 'H', 'THREE')
        nlist, llist = extract_digits(nlist, llist, '4', 'R', 'FOUR')
        nlist, llist = extract_digits(nlist, llist, '5', 'F', 'FIVE')
        nlist, llist = extract_digits(nlist, llist, '1', 'O', 'ONE')
        nlist, llist = extract_digits(nlist, llist, '7', 'V', 'SEVEN')
        nlist, llist = extract_digits(nlist, llist, '9', 'I', 'NINE')

        print "Case #%d: %s" % (i, ''.join(str(x) for x in sorted(nlist)))
