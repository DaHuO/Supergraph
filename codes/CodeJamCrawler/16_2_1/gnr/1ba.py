__author__ = 'dilip'

from copy import deepcopy

zero = ['Z', 'E','R', 'O']
one = ['O', 'N', 'E']
two = ['T', 'W', 'O']
three = ['T', 'H','R', 'E', 'E']
four = ['F', 'O','U', 'R']
five = ['F', 'I','V', 'E']
six = ['S', 'I','X']
seven = ['S', 'E','V', 'E', 'N']
eight = ['E', 'I','G', 'H', 'T']
nine = ['N', 'I','N', 'E']

checklist = [ seven, nine, one]

nummapping = {
    'ZERO': 0,
    'TWO': 2,
    'SIX': 6,
    'FOUR': 4,
    'FIVE': 5,
    'SEVEN': 7,
    'EIGHT': 8,
    'THREE': 3,
    'NINE': 9,
    'ONE': 1,

}

def checksublist(big, small):
    newbig = deepcopy(big)
    done = True
    for ch in small:
        if ch in big:
            newbig.remove(ch)
            continue
        else:
            return None
    return newbig

def findnumber(s):
    numberlist = []
    chset = [a for a in s]

    while len(chset) != 0:
        if 'Z' in chset:
            newlist = checksublist(chset, zero)
            if newlist is not None:
                numberlist.append(0)
                chset = newlist

        elif 'W' in chset:
            newlist = checksublist(chset, two)
            if newlist is not None:
                numberlist.append(2)
                chset = newlist
        elif 'X' in chset:
            newlist = checksublist(chset, six)
            if newlist is not None:
                numberlist.append(6)
                chset = newlist
        elif 'U' in chset:
            newlist = checksublist(chset, four)
            if newlist is not None:
                numberlist.append(4)
                chset = newlist

        elif 'G' in chset:
            newlist = checksublist(chset, eight)
            if newlist is not None:
                numberlist.append(8)
                chset = newlist

        elif 'V' in chset and 'S' not in chset:
            newlist = checksublist(chset, five)
            if newlist is not None:
                numberlist.append(5)
                chset = newlist

        elif 'H' in chset and 'R' in chset and 'I' not in chset:
            newlist = checksublist(chset, three)
            if newlist is not None:
                numberlist.append(3)
                chset = newlist

        elif 'S' in chset and 'V' in chset:
            newlist = checksublist(chset, seven)
            if newlist is not None:
                numberlist.append(7)
                chset = newlist

        elif 'N' in chset and 'O' not in chset:
            newlist = checksublist(chset, nine)
            if newlist is not None:
                numberlist.append(9)
                chset = newlist

        elif 'N' in chset and 'O' in chset:
            newlist = checksublist(chset, one)
            if newlist is not None:
                numberlist.append(1)
                chset = newlist

        if len(chset) == 0:
            break
    numberlist.sort()
    return ''.join([str(number) for number in numberlist])





with open('A-large.in') as in_file:
    t = int(in_file.readline())
    with open('A-large.out', 'w') as out_file:
        for i in xrange(1, t+1):
            n = in_file.readline().strip()
            lastname = findnumber(n)
            out_file.write('Case #{0}: {1}\n'.format(i, lastname))
