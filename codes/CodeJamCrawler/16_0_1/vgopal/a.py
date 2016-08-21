def answer(N):
    if N == 0:
        return 'INSOMNIA'
    num = 0
    digits_seen = set()
    while len(digits_seen) < 10:
        num += N
        digits_seen.update(list(str(num)))
    return num

input_file = open('a-large.txt')
input_file.readline()
for input_num, line in enumerate(input_file):
    N = int(line)
    print "Case #{}: {}".format(input_num + 1, answer(N))
