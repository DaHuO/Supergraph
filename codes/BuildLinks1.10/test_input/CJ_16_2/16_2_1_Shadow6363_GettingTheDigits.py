import collections
import sys

NUMBERS = {
    'ZERO': '0',
    'ONE': '1',
    'TWO': '2',
    'THREE': '3',
    'FOUR': '4',
    'FIVE': '5',
    'SIX': '6',
    'SEVEN': '7',
    'EIGHT': '8',
    'NINE': '9'
}

LENGTHS = {
    'ZERO': 4,
    'ONE': 3,
    'TWO': 3,
    'THREE': 5,
    'FOUR': 4,
    'FIVE': 4,
    'SIX': 3,
    'SEVEN': 5,
    'EIGHT': 5,
    'NINE': 4
}

EVENS = {
    'Z': 'ZERO',
    'W': 'TWO',
    'U': 'FOUR',
    'X': 'SIX',
    'G': 'EIGHT'
}

ODDS = {
    'F': 'FIVE',
    'H': 'THREE',
    'N': 'NINE',
    'O': 'ONE',
    'S': 'SEVEN'
}

blank = collections.Counter()


def check_letter(letter_counts, letter):


    return letter_counts


def main():
    T = int(sys.stdin.readline().strip())
    for case in xrange(T):
        letter_counts = collections.Counter(sys.stdin.readline().strip())

        evens = True
        phone_no = []

        while letter_counts:
            if evens:
                evens = False
                for letter, number in EVENS.iteritems():
                    if letter in letter_counts:
                        letter_counts.subtract(number)
                        phone_no.append(NUMBERS[number])

                        if letter_counts[letter] == 0:
                            letter_counts += blank
                        else:
                            evens = True
            else:
                for letter in ('H', 'O', 'S', 'F', 'N'):
                    if letter in letter_counts:
                        letter_counts.subtract(ODDS[letter])
                        phone_no.append(NUMBERS[ODDS[letter]])

                        if letter_counts[letter] == 0:
                            letter_counts += blank

                        break

        print 'Case #{0}: {1}'.format(case+1, ''.join(sorted(phone_no)))


if __name__ == '__main__':
    main()
