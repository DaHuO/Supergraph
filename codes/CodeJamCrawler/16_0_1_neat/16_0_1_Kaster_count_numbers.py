import sys
def counting_numbers(n, case, i = 1, already_have = set()):
    if (n == 0):
        message = 'Case #%d: %s' % (case, 'INSOMNIA')
    else:
        N = str(i * n)
        unique_nums = set(list(N))
        combined = unique_nums | already_have
        if len(combined) < 10:
            message = counting_numbers(n, case, i + 1, combined)
        else:
            message = 'Case #%d: %s' % (case, n*i)
    return message

def check_answer(n, i = 1, already_have = set()):
    if (n == 0):
        print 'INSOMNIA'
    else:
        N = str(i * n)
        unique_nums = set(list(N))
        print 'number: %d' % (n * i), 'unique digits: ' + str(unique_nums), 'seen before: ' + str(already_have)
        sys.stdout.flush()
        combined = unique_nums | already_have
        if len(combined) < 10:
            raw_input()
            check_answer(n, i + 1, combined)

# open the file
with open('A-large.in', 'r') as f:
    small = [int(a) for a in f.read().split('\n')[:-1]]

T = small[0]
out = ''
for i, number in enumerate(small[1:]):
    out += counting_numbers(number, i+1) + '\n'

open('output2.txt', 'w').write(out)

# check_answer(11)