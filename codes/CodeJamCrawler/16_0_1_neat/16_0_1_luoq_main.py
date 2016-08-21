import sys
def run(f):
    infile_name = sys.argv[1]
    outfile_name = infile_name+'.out'
    with open(outfile_name, 'w') as outfile:
        for i, line in enumerate(open(infile_name)):
            if i == 0:
                continue
            outfile.write('Case #{}: {}\n'.format(i, f(line)))

def counting_sheep(line):
    n = int(line)

    if n == 0:
        return 'INSOMNIA'

    x = n
    
    seen_digits = set()
    while len(seen_digits) < 10:
        seen_digits.update(set(str(x)))
        x += n

    return x-n


if __name__ == '__main__':
    run(counting_sheep)
