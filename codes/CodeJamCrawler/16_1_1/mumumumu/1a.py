def append_both(letter, initial_word, new_word):
    if len(initial_word) == 0:
        res = [letter + new_word] + [new_word + letter]
        return res
    else:
        return append_both(initial_word[0], initial_word[1:], new_word + letter) + \
            append_both(initial_word[0], initial_word[1:], letter + new_word)


def get_output(i):
    possible_words = append_both(i[0], i[1:], '')
    return sorted(possible_words, reverse=True)[0]

with open('1A-small-attempt0.in', 'r') as f:
    _input = [line.strip() for line in f.readlines()]
    num_test_cases = _input[0]
    _input = _input[1:]
    with open('output.txt', 'w') as fo:
        for i, line in enumerate(_input):
            out = 'Case #' + str(i + 1) + ': ' + str(get_output(line)) + '\n'
            fo.write(out)
