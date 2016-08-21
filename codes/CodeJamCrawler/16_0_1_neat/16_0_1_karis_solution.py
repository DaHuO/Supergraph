from itertools import count

with open('A-large.in') as input:
    lines = input.readlines()
    T = lines[0]

with open('output.txt', 'wt') as output:
    for i in range(1, int(T) + 1):
        N = int(lines[i])
        if N == 0:
            output.write("Case #{}: INSOMNIA\n".format(i))
        else:
            digits = set()
            for j in count(start = 1):
                C = N * j
                digits.update([int(k) for k in str(C)])
                if len(digits) == 10:
                    output.write("Case #{}: {}\n".format(i, C))
                    break;

