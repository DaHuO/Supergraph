

def sleep(N):
    def iter_digits(N):
        while N > 0:
            yield N % 10
            N /= 10

    if N == 0:
        return 'INSOMNIA'

    seen_digits = set()
    i = 1
    while True:
        for digit in iter_digits(N * i):
            seen_digits.update([digit])
            if len(seen_digits) == 10:
                return N * i
        i += 1

# for N in [0, 1, 2, 11, 1692]:
with open('A-large.in', 'r') as small_file, open('output.txt', 'w') \
        as output_file:
    for index, N in enumerate(small_file.readlines()[1:]):
        N = N.strip()
        output_file.write('Case #{}: {}'.format(index+1, sleep(int(N))))
        output_file.write('\n')
