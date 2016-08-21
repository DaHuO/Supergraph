def perms_word(word):
    if len(word) < 1:
        return None
    def rec(words, idx):
        arr = []
        if idx < len(word):
            for w in words:
                arr.append(w + word[idx])
                arr.append(word[idx] + w)
            return rec(arr, idx + 1)
        else:
            return words
        return arr
    return rec([word[0]], 1)


def gen_string(word):
    words = perms_word(word)
    if words:
        sorted_words = sorted(words)
        return sorted_words[len(words) - 1]

        

def load_input(filename = None):
    if not filename:
        return
    line_buffer = None
    with open(filename, 'r+') as f:
        line_buffer = f.read().splitlines()
    f.close()
    return line_buffer

import sys  

def main(argv):
    if not argv:
        filename = __file__
        lines = ['1', 'ZXCASDQWE']
    else:
        filename = argv[0]
        lines = load_input(filename + '.in')
    f = open(filename + '.out', 'w+')
    for i in xrange(int(lines[0])):
        # N, J = map(str, lines[i + 1].split(' '))
        init_word = lines[i + 1]
        last_word = gen_string(init_word)
        s =  'Case #%d: %s\n'%(i+1, last_word)
        f.writelines(s)
        print '%s'%s
    f.close()

if __name__ == '__main__':
    main(sys.argv[1:])