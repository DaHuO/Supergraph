input_file = open('A-large.in', 'r')
out_file = open('A-res-large.out', 'w')

test_cases = int(input_file.readline())

for t in range(1, test_cases + 1):

    s = input_file.readline().strip()
    res = s[0]

    for i in range(1, len(s)):
        if s[i] >= res[0]:
            res = s[i] + res
        else:
            res = res + s[i]


    out_file.write('Case #{:d}: {:s}\n'.format(t, res))

