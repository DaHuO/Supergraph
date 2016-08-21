import sys


def last_word(word_line):
    word_line = word_line.strip()
    new_word = [word_line[0]]
    for e in word_line[1:]:
        if e >= new_word[0]:
            new_word = [e] + new_word
        else:
            new_word.append(e)
    return ''.join(new_word)
    
if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        print "Case #%d:" % (i + 1),
        word_line = sys.stdin.readline()
        print last_word(word_line)


