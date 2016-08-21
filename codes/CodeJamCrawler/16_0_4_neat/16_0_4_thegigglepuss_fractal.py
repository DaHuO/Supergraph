import sys

def generate(length, complexity):
    first = 1
    last = 2 ** length
    current = first
    form = '{0:0' + str(length) + 'b}'
    original_comp = complexity
    return_val = []
    while current < last:
        original = form.format(current)
        complexity = original_comp
        result = original
        while complexity > 1:
            next_result = ''
            for c in result:
                if c == '1':
                    next_result += '111'
                else:
                    next_result += original
            result = next_result
            complexity -= 1
        return_val.append(result)
        current += 1
    return return_val

def solve(k, c):
    length = k ** c
    per = length / k
    solution = 1
    solutions = []
    while solution < length:
        solutions.append(str(solution))
        solution += per
    return solutions


    # sequences = generate(k, c)
    # end_length = len(sequences[0])
    # test_vals = []
    # for p in range(0, end_length):
    #     test_vals.append(2 ** p)
    # needed = []
    # while len(sequences) > 0:
    #     best = []
    #     best_idx = -1
    #     for idx, test in enumerate(test_vals):
    #         remove = []
    #         for s in sequences:
    #             if int(s, 2) & test != 0:
    #                 remove.append(s)
    #         if len(remove) > len(best):
    #             best = remove
    #             best_idx = idx
    #     for i in best:
    #         sequences.remove(i)
    #     needed.append(str(best_idx + 1))
    # return needed

with open(sys.argv[1], 'r') as f:
    lines = int(f.readline())
    count = 1
    for line in f:
        vals = line.split(' ')
        k = int(vals[0])
        c = int(vals[1])
        s = int(vals[2])
        if k == 1:
            answer = '1'
        elif c == 1 and s == k:
            answer = []
            for x in range(1, k + 1):
                answer.append(str(x))
            answer = ' '.join(answer)
        elif s < k:
            answer = 'IMPOSSIBLE'
        else:
            sol = solve(k, c)
            if len(sol) > s:
                answer = 'IMPOSSIBLE'
            else:
                answer = ' '.join(sol)
        print "Case #{}: {}".format(count, answer)
        count += 1

#generate all final sequences with Gs
#for each G, remove all sequences with that G
    #repeat for resulting sequences until none remain