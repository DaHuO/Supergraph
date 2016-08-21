input_file = "A-large.in"
output_file = "result.out"

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
help_order = ['Z', 'W', 'X', 'S', 'V', 'G', 'H', 'U', 'O', 'I']
help = {'Z': (0, ['O']), 'W': (2, ['O']), 'X': (6, ['I', 'S']), 'S': (7, ['V']), 'V': (5, ['I']), 'G': (8, ['H', 'I']), 'H': (3, []), 'U': (4, ['O']), 'O': (1, []), 'I': (9, [])}

with open(input_file) as in_file, open(output_file, 'w') as out_file:
    testcases = int(in_file.readline())
    for i in range(1, testcases + 1):

        char_dict = {}
        for c in list(in_file.readline()):
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] += 1

        res = []
        for cur_key in help_order:
            if cur_key not in char_dict:
                continue
            cur_value = help[cur_key]
            res += [cur_value[0]] * char_dict[cur_key]
            for c in cur_value[1]:
                if c not in char_dict:
                    continue
                char_dict[c] -= char_dict[cur_key]

        res.sort()
        out_file.write('Case #{}: {}\n'.format(i, ''.join([str(r) for r in res])))
