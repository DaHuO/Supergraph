import collections


def parse(s):
    letter_freq = collections.Counter(s)
    number_freq = collections.defaultdict(int)

    # ZERO
    while 'Z' in letter_freq and letter_freq['Z'] > 0:
        letter_freq['Z'] -= 1
        letter_freq['E'] -= 1
        letter_freq['R'] -= 1
        letter_freq['O'] -= 1
        number_freq[0] += 1

    # TWO
    while 'W' in letter_freq and letter_freq['W'] > 0:
        letter_freq['T'] -= 1
        letter_freq['W'] -= 1
        letter_freq['O'] -= 1
        number_freq[2] += 1

    # FOUR
    while 'U' in letter_freq and letter_freq['U'] > 0:
        letter_freq['F'] -= 1
        letter_freq['O'] -= 1
        letter_freq['U'] -= 1
        letter_freq['R'] -= 1
        number_freq[4] += 1

    # SIX
    while 'X' in letter_freq and letter_freq['X'] > 0:
        letter_freq['S'] -= 1
        letter_freq['I'] -= 1
        letter_freq['X'] -= 1
        number_freq[6] += 1

    # EIGHT
    while 'G' in letter_freq and letter_freq['G'] > 0:
        letter_freq['E'] -= 1
        letter_freq['I'] -= 1
        letter_freq['G'] -= 1
        letter_freq['H'] -= 1
        letter_freq['T'] -= 1
        number_freq[8] += 1

    # ONE
    while 'O' in letter_freq and letter_freq['O'] > 0:
        letter_freq['O'] -= 1
        letter_freq['N'] -= 1
        letter_freq['E'] -= 1
        number_freq[1] += 1

    # THREE
    while 'R' in letter_freq and letter_freq['R'] > 0:
        letter_freq['T'] -= 1
        letter_freq['H'] -= 1
        letter_freq['R'] -= 1
        letter_freq['E'] -= 2
        number_freq[3] += 1

    # FIVE
    while 'F' in letter_freq and letter_freq['F'] > 0:
        letter_freq['F'] -= 1
        letter_freq['I'] -= 1
        letter_freq['V'] -= 1
        letter_freq['E'] -= 1
        number_freq[5] += 1

    # SEVEN
    while 'S' in letter_freq and letter_freq['S'] > 0:
        letter_freq['S'] -= 1
        letter_freq['E'] -= 2
        letter_freq['V'] -= 1
        letter_freq['N'] -= 1
        number_freq[7] += 1

    # NINE
    while 'N' in letter_freq and letter_freq['N'] > 0:
        letter_freq['N'] -= 2
        letter_freq['I'] -= 1
        letter_freq['E'] -= 1
        number_freq[9] += 1

    retval = ''
    for x in xrange(10):
        retval += (number_freq[x]*str(x))

    return retval


def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    open(output_filename, 'wb').close()
    with open(input_filename, 'r+b') as f:
        with open(output_filename, 'r+b') as g:
            t = int(f.readline().strip())
            for i in range(1, t+1):
                s = f.readline().strip()
                answer = parse(s)
                print("Case #%d: %s" % (i, answer))
                g.write("Case #%d: %s\n" % (i, answer))


if __name__ == '__main__':
    main()