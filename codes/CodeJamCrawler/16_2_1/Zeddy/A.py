if __name__ == "__main__":

    fin = open('A-large.in', 'r')
    fout = open('A-large.out', 'w')

    #fin = open('in.txt', 'r')
    #fout = open('out.txt', 'w')

    cases = int(fin.readline())
    print cases

    for t in range(0, cases):
        letter_count = {}
        number_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        s = list(fin.readline().rstrip())

        for letter in s:
            if letter.lower() in letter_count:
                letter_count[letter.lower()] += 1
            else:
                letter_count[letter.lower()] = 1

        if 'z' in letter_count:
            if letter_count['z'] > 0:
                number_count[0] += letter_count['z']
                letter_count['z'] -= number_count[0]
                letter_count['e'] -= number_count[0]
                letter_count['r'] -= number_count[0]
                letter_count['o'] -= number_count[0]

        if 'w' in letter_count:
            if letter_count['w'] > 0:
                number_count[2] += letter_count['w']
                letter_count['t'] -= number_count[2]
                letter_count['w'] -= number_count[2]
                letter_count['o'] -= number_count[2]

        if 'u' in letter_count:
            if letter_count['u'] > 0:
                number_count[4] += letter_count['u']
                letter_count['f'] -= number_count[4]
                letter_count['o'] -= number_count[4]
                letter_count['u'] -= number_count[4]
                letter_count['r'] -= number_count[4]

        if 'x' in letter_count:
            if letter_count['x'] > 0:
                number_count[6] += letter_count['x']
                letter_count['s'] -= number_count[6]
                letter_count['i'] -= number_count[6]
                letter_count['x'] -= number_count[6]

        if 'g' in letter_count:
            if letter_count['g'] > 0:
                number_count[8] += letter_count['g']
                letter_count['e'] -= number_count[8]
                letter_count['i'] -= number_count[8]
                letter_count['g'] -= number_count[8]
                letter_count['h'] -= number_count[8]
                letter_count['t'] -= number_count[8]

        if 'o' in letter_count:
            if letter_count['o'] > 0:
                number_count[1] += letter_count['o']
                letter_count['o'] -= number_count[1]
                letter_count['n'] -= number_count[1]
                letter_count['e'] -= number_count[1]

        if 'r' in letter_count:
            if letter_count['r'] > 0:
                number_count[3] += letter_count['r']
                letter_count['t'] -= number_count[3]
                letter_count['h'] -= number_count[3]
                letter_count['r'] -= number_count[3]
                letter_count['e'] -= number_count[3]
                letter_count['e'] -= number_count[3]

        if 'f' in letter_count:
            if letter_count['f'] > 0:
                number_count[5] += letter_count['f']
                letter_count['f'] -= number_count[5]
                letter_count['i'] -= number_count[5]
                letter_count['v'] -= number_count[5]
                letter_count['e'] -= number_count[5]

        if 'v' in letter_count:
            if letter_count['v'] > 0:
                number_count[7] += letter_count['v']
                letter_count['s'] -= number_count[7]
                letter_count['e'] -= number_count[7]
                letter_count['v'] -= number_count[7]
                letter_count['e'] -= number_count[7]
                letter_count['n'] -= number_count[7]

        if 'i' in letter_count:
            number_count[9] += letter_count['i']

        phone_num = ''
        cur_digit = 0
        for digit in number_count:
            for i in range(0, digit):
                phone_num += str(cur_digit)
            cur_digit += 1

        print "Case #%d: %s" % (t+1, phone_num)
        fout.write("Case #" + str(t+1) + ": " + phone_num + "\n")

    fin.close()
    fout.close()