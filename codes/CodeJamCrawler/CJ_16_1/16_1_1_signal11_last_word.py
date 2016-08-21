import sys

def final_word(S):
    word_list = []

    for l in S:
        if len(word_list) == 0:
            word_list.append(l)
        else:
            new_wordlist = []
            for w in word_list:
                new_word_1 = l+w
                new_word_2 = w+l

                new_wordlist.append(new_word_1)
                if new_word_1 != new_word_2:
                    new_wordlist.append(new_word_2)

            # for w in word_list
            word_list = new_wordlist[:]

    word_list.sort()
    return word_list[-1]


def main():
    num_tests = int(sys.stdin.readline())
    for tc in xrange(1, num_tests+1):
        S = raw_input()
        print "Case #" + str(tc) + ": " + final_word(S)

    return

if __name__ == "__main__":
    main()
