import sys


want = range(10)

def handle_case(line):
    S = line.strip()
    Siter = iter(S)
    final_word = [next(Siter)]
    for letter in Siter:
        if letter < final_word[0]:
            final_word.append(letter)
        else:
            final_word.insert(0, letter)
    return ''.join(final_word)

if __name__ == '__main__':
    cases = int(sys.stdin.readline().strip())

    for i in xrange(1, cases+1):
        line = sys.stdin.readline().strip()
        answer = handle_case(line)
        print "Case #{}: {}".format(i, answer)
