def explode_num(n):
    digits = set()
    while n > 0:
        digits.add(n % 10)
        n = int(n / 10)
    return digits


def count(n):
    if n == 0:
        return 'INSOMNIA'
    seen = explode_num(n)
    i = 2
    while len(seen) < 10:
        seen = seen.union(explode_num(i * n))
        i += 1
    return (i - 1) * n


def run():
    with open('A-large.in', 'r') as infile, open('outL.txt', 'w') as outfile:
        num_cases = int(infile.readline())
        for i in range(1, num_cases+1):
            outfile.write('Case #' + str(i) + ': ')
            outfile.write(str(count(int(infile.readline()))))
            outfile.write('\n')


run()
